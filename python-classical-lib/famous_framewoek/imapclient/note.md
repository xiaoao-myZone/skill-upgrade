imapclient.IMAPCLIENT('imap.163.com',ssl=True)返回的对象经过登录后可使用
select_folder('document_name',readonly=True)
再然后使用search([''])方法的的搜索键：

'ALL'：返回该文件夹中的所有文件，但是有大小限制

'BEFORE date'/'ON date'/'SINCE date'：date的格式必须是05-Jul-2015,before是开区间，since是闭区间

'SUBJECT string'/'BODY string':查找存在string的主题、正文中的消息，如果string中有空格，'TEXT"search with space"'

'TEXT string':查找存在string的主题或正文中的消息


'FROM string'/'TO string'/'CC string'/'BCC string':返回所有消息，如有多个邮件地址用空格隔开
           'CC "fist second"'




search(criteria='ALL', charset=None) method of imapclient.imapclient.IMAPClient instance
    Return a list of messages ids from the currently selected
    folder matching *criteria*.
    
    *criteria* should be a sequence of one or more criteria
    items. Each criteria item may be either unicode or
    bytes. Example values::
    
        [u'UNSEEN']
        [u'SMALLER', 500]
        [b'NOT', b'DELETED']
        [u'TEXT', u'foo bar', u'FLAGGED', u'SUBJECT', u'baz']
        [u'SINCE', date(2005, 4, 3)]
    
    IMAPClient will perform conversion and quoting as
    required. The caller shouldn't do this.
    
    It is also possible (but not recommended) to pass the combined
    criteria as a single string. In this case IMAPClient won't
    perform quoting, allowing lower-level specification of
    criteria. Examples of this style::
    
        u'UNSEEN'
        u'SMALLER 500'
        b'NOT DELETED'
        u'TEXT "foo bar" FLAGGED SUBJECT "baz"'
        b'SINCE 03-Apr-2005'
    
    To support complex search expressions, criteria lists can be
    nested. IMAPClient will insert parentheses in the right
    places. The following will match messages that are both not
    flagged and do not have "foo" in the subject:
    
        ['NOT', ['SUBJECT', 'foo', 'FLAGGED']]
    
    *charset* specifies the character set of the criteria. It
    defaults to US-ASCII as this is the only charset that a server
    is required to support by the RFC. UTF-8 is commonly supported
    however.
    
    Any criteria specified using unicode will be encoded as per
    *charset*. Specifying a unicode criteria that can not be
    encoded using *charset* will result in an error.
    
    Any criteria specified using bytes will be sent as-is but
    should use an encoding that matches *charset* (the character
    set given is still passed on to the server).
    
    See :rfc:`3501#section-6.4.4` for more details.
    
    Note that criteria arguments that are 8-bit will be
    transparently sent by IMAPClient as IMAP literals to ensure
    adherence to IMAP standards.
    
    The returned list of message ids will have a special *modseq*
    attribute. This is set if the server included a MODSEQ value
    to the search response (i.e. if a MODSEQ criteria was included
    in the search)

·························
    def delete_messages(self, messages, silent=False):
        """Delete one or more *messages* from the currently selected
        folder.

        Returns the flags set for each modified message (see
        *get_flags*).
        """
        return self.add_flags(messages, DELETED, silent=silent)

    def add_flags(self, messages, flags, silent=False):
        """Add *flags* to *messages* in the currently selected folder.

        *flags* should be a sequence of strings.

        Returns the flags set for each modified message (see
        *get_flags*), or None if *silent* is true.
        """
        return self._store(b'+FLAGS', messages, flags, b'FLAGS', silent=silent)

    def _store(self, cmd, messages, flags, fetch_key, silent):
        """Worker function for the various flag manipulation methods.

        *cmd* is the STORE command to use (eg. '+FLAGS').
        """
        if not messages:
            return {}
        if silent:
            cmd += b".SILENT"

        data = self._command_and_check('store',
                                       join_message_ids(messages),
                                       cmd,
                                       seq_to_parenstr(flags),
                                       uid=True)
        if silent:
            return None
        return self._filter_fetch_dict(parse_fetch_response(data),
                                       fetch_key)

def _command_and_check(self, command, *args, **kwargs):
        unpack = pop_with_default(kwargs, 'unpack', False)
        uid = pop_with_default(kwargs, 'uid', False)
        assert not kwargs, "unexpected keyword args: " + ', '.join(kwargs)

        if uid and self.use_uid:
            if PY3:
                command = to_unicode(command)  # imaplib must die
            typ, data = self._imap.uid(command, *args)
        else:
            meth = getattr(self._imap, to_unicode(command))
            typ, data = meth(*args)
        self._checkok(command, typ, data)
        if unpack:
            return data[0]
        return data

DELETED = br'\Deleted'
