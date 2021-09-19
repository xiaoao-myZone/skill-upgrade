plot(*args, scalex=True, scaley=True, data=None, **kwargs)
    Plot y versus x as lines and/or markers.
    
    Call signatures::
    
        plot([x], y, [fmt], data=None, **kwargs)
        plot([x], y, [fmt], [x2], y2, [fmt2], ..., **kwargs)
    
    The coordinates of the points or line nodes are given by *x*, *y*.
    
    The optional parameter *fmt* is a convenient way for defining basic
    formatting like color, marker and linestyle. It's a shortcut string
    notation described in the *Notes* section below.
    
    >>> plot(x, y)        # plot x and y using default line style and color
    >>> plot(x, y, 'bo')  # plot x and y using blue circle markers
    >>> plot(y)           # plot y using x as index array 0..N-1
    >>> plot(y, 'r+')     # ditto, but with red plusses
    
    You can use `.Line2D` properties as keyword arguments for more
    control on the appearance. Line properties and *fmt* can be mixed.
    The following two calls yield identical results:
    
    >>> plot(x, y, 'go--', linewidth=2, markersize=12)
    >>> plot(x, y, color='green', marker='o', linestyle='dashed',
    ...      linewidth=2, markersize=12)
    
    When conflicting with *fmt*, keyword arguments take precedence.
    
    **Plotting labelled data**
    
    There's a convenient way for plotting objects with labelled data (i.e.
    data that can be accessed by index ``obj['y']``). Instead of giving
    the data in *x* and *y*, you can provide the object in the *data*
    parameter and just give the labels for *x* and *y*::
    
    >>> plot('xlabel', 'ylabel', data=obj)
    
    All indexable objects are supported. This could e.g. be a `dict`, a
    `pandas.DataFame` or a structured numpy array.
    
    
    **Plotting multiple sets of data**
    
    There are various ways to plot multiple sets of data.
    
    - The most straight forward way is just to call `plot` multiple times.
      Example:
    
      >>> plot(x1, y1, 'bo')
      >>> plot(x2, y2, 'go')
    
    - Alternatively, if your data is already a 2d array, you can pass it
      directly to *x*, *y*. A separate data set will be drawn for every
      column.
    
      Example: an array ``a`` where the first column represents the *x*
      values and the other columns are the *y* columns::
    
      >>> plot(a[0], a[1:])
    
    - The third way is to specify multiple sets of *[x]*, *y*, *[fmt]*
      groups::
    
      >>> plot(x1, y1, 'g^', x2, y2, 'g-')
    
      In this case, any additional keyword argument applies to all
      datasets. Also this syntax cannot be combined with the *data*
      parameter.
    
    By default, each line is assigned a different style specified by a
    'style cycle'. The *fmt* and line property parameters are only
    necessary if you want explicit deviations from these defaults.
    Alternatively, you can also change the style cycle using the
    'axes.prop_cycle' rcParam.
    
    Parameters
    ----------
    x, y : array-like or scalar
        The horizontal / vertical coordinates of the data points.
        *x* values are optional. If not given, they default to
        ``[0, ..., N-1]``.
    
        Commonly, these parameters are arrays of length N. However,
        scalars are supported as well (equivalent to an array with
        constant value).
    
        The parameters can also be 2-dimensional. Then, the columns
        represent separate data sets.
    
    fmt : str, optional
        A format string, e.g. 'ro' for red circles. See the *Notes*
        section for a full description of the format strings.
    
        Format strings are just an abbreviation for quickly setting
        basic line properties. All of these and more can also be
        controlled by keyword arguments.
    
    data : indexable object, optional
        An object with labelled data. If given, provide the label names to
        plot in *x* and *y*.
    
        .. note::
            Technically there's a slight ambiguity in calls where the
            second label is a valid *fmt*. `plot('n', 'o', data=obj)`
            could be `plt(x, y)` or `plt(y, fmt)`. In such cases,
            the former interpretation is chosen, but a warning is issued.
            You may suppress the warning by adding an empty format string
            `plot('n', 'o', '', data=obj)`.
    
    
    Other Parameters
    ----------------
    scalex, scaley : bool, optional, default: True
        These parameters determined if the view limits are adapted to
        the data limits. The values are passed on to `autoscale_view`.
    
    **kwargs : `.Line2D` properties, optional
        *kwargs* are used to specify properties like a line label (for
        auto legends), linewidth, antialiasing, marker face color.
        Example::
    
        >>> plot([1,2,3], [1,2,3], 'go-', label='line 1', linewidth=2)
        >>> plot([1,2,3], [1,4,9], 'rs',  label='line 2')
    
        If you make multiple lines with one plot command, the kwargs
        apply to all those lines.
    
        Here is a list of available `.Line2D` properties:
    
          agg_filter: a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array 
      alpha: float
      animated: bool
      antialiased: bool
      clip_box: `.Bbox`
      clip_on: bool
      clip_path: [(`~matplotlib.path.Path`, `.Transform`) | `.Patch` | None] 
      color: color
      contains: callable
      dash_capstyle: {'butt', 'round', 'projecting'}
      dash_joinstyle: {'miter', 'round', 'bevel'}
      dashes: sequence of floats (on/off ink in points) or (None, None)
      drawstyle: {'default', 'steps', 'steps-pre', 'steps-mid', 'steps-post'}
      figure: `.Figure`
      fillstyle: {'full', 'left', 'right', 'bottom', 'top', 'none'}
      gid: str
      in_layout: bool
      label: object
      linestyle: {'-', '--', '-.', ':', '', (offset, on-off-seq), ...}
      linewidth: float
      marker: unknown
      markeredgecolor: color
      markeredgewidth: float
      markerfacecolor: color
      markerfacecoloralt: color
      markersize: float
      markevery: unknown
      path_effects: `.AbstractPathEffect`
      picker: float or callable[[Artist, Event], Tuple[bool, dict]]
      pickradius: float
      rasterized: bool or None
      sketch_params: (scale: float, length: float, randomness: float) 
      snap: bool or None
      solid_capstyle: {'butt', 'round', 'projecting'}
      solid_joinstyle: {'miter', 'round', 'bevel'}
      transform: matplotlib.transforms.Transform
      url: str
      visible: bool
      xdata: 1D array
      ydata: 1D array
      zorder: float
    
    Returns
    -------
    lines
        A list of `.Line2D` objects representing the plotted data.
    
    
    See Also
    --------
    scatter : XY scatter plot with markers of varying size and/or color (
        sometimes also called bubble chart).
    
    
    Notes
    -----
    **Format Strings**
    
    A format string consists of a part for color, marker and line::
    
        fmt = '[color][marker][line]'
    
    Each of them is optional. If not provided, the value from the style
    cycle is used. Exception: If ``line`` is given, but no ``marker``,
    the data will be a line without markers.
    
    **Colors**
    
    The following color abbreviations are supported:
    
    =============    ===============================
    character        color
    =============    ===============================
    ``'b'``          blue
    ``'g'``          green
    ``'r'``          red
    ``'c'``          cyan
    ``'m'``          magenta
    ``'y'``          yellow
    ``'k'``          black
    ``'w'``          white
    =============    ===============================
    
    If the color is the only part of the format string, you can
    additionally use any  `matplotlib.colors` spec, e.g. full names
    (``'green'``) or hex strings (``'#008000'``).
    
    **Markers**
    
    =============    ===============================
    character        description
    =============    ===============================
    ``'.'``          point marker
    ``','``          pixel marker
    ``'o'``          circle marker
    ``'v'``          triangle_down marker
    ``'^'``          triangle_up marker
    ``'<'``          triangle_left marker
    ``'>'``          triangle_right marker
    ``'1'``          tri_down marker
    ``'2'``          tri_up marker
    ``'3'``          tri_left marker
    ``'4'``          tri_right marker
    ``'s'``          square marker
    ``'p'``          pentagon marker
    ``'*'``          star marker
    ``'h'``          hexagon1 marker
    ``'H'``          hexagon2 marker
    ``'+'``          plus marker
    ``'x'``          x marker
    ``'D'``          diamond marker
    ``'d'``          thin_diamond marker
    ``'|'``          vline marker
    ``'_'``          hline marker
    =============    ===============================
    
    **Line Styles**
    
    =============    ===============================
    character        description
    =============    ===============================
    ``'-'``          solid line style
    ``'--'``         dashed line style
    ``'-.'``         dash-dot line style
    ``':'``          dotted line style
    =============    ===============================
    
    Example format strings::
    
        'b'    # blue markers with default shape
        'ro'   # red circles
        'g-'   # green solid line
        '--'   # dashed line with default color
        'k^:'  # black triangle_up markers connected by a dotted line
    
    .. note::
        In addition to the above described arguments, this function can take a
        **data** keyword argument. If such a **data** argument is given, the
        following arguments are replaced by **data[<arg>]**:
    
        * All arguments with the following names: 'x', 'y'.
    
        Objects passed as **data** must support item access (``data[<arg>]``) and
        membership test (``<arg> in data``).




Help on function scatter in module matplotlib.pyplot:

scatter(x, y, s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, verts=None, edgecolors=None, *, data=None, **kwargs)
    A scatter plot of *y* vs *x* with varying marker size and/or color.
    
    Parameters
    ----------
    x, y : array_like, shape (n, )
        The data positions.
    
    s : scalar or array_like, shape (n, ), optional
        The marker size in points**2.
        Default is ``rcParams['lines.markersize'] ** 2``.
    
    c : color, sequence, or sequence of color, optional
        The marker color. Possible values:
    
        - A single color format string.
        - A sequence of color specifications of length n.
        - A sequence of n numbers to be mapped to colors using *cmap* and
          *norm*.
        - A 2-D array in which the rows are RGB or RGBA.
    
        Note that *c* should not be a single numeric RGB or RGBA sequence
        because that is indistinguishable from an array of values to be
        colormapped. If you want to specify the same RGB or RGBA value for
        all points, use a 2-D array with a single row.  Otherwise, value-
        matching will have precedence in case of a size matching with *x*
        and *y*.
    
        Defaults to ``None``. In that case the marker color is determined
        by the value of ``color``, ``facecolor`` or ``facecolors``. In case
        those are not specified or ``None``, the marker color is determined
        by the next color of the ``Axes``' current "shape and fill" color
        cycle. This cycle defaults to :rc:`axes.prop_cycle`.
    
    marker : `~matplotlib.markers.MarkerStyle`, optional
        The marker style. *marker* can be either an instance of the class
        or the text shorthand for a particular marker.
        Defaults to ``None``, in which case it takes the value of
        :rc:`scatter.marker` = 'o'.
        See `~matplotlib.markers` for more information about marker styles.
    
    cmap : `~matplotlib.colors.Colormap`, optional, default: None
        A `.Colormap` instance or registered colormap name. *cmap* is only
        used if *c* is an array of floats. If ``None``, defaults to rc
        ``image.cmap``.
    
    norm : `~matplotlib.colors.Normalize`, optional, default: None
        A `.Normalize` instance is used to scale luminance data to 0, 1.
        *norm* is only used if *c* is an array of floats. If *None*, use
        the default `.colors.Normalize`.
    
    vmin, vmax : scalar, optional, default: None
        *vmin* and *vmax* are used in conjunction with *norm* to normalize
        luminance data. If None, the respective min and max of the color
        array is used. *vmin* and *vmax* are ignored if you pass a *norm*
        instance.
    
    alpha : scalar, optional, default: None
        The alpha blending value, between 0 (transparent) and 1 (opaque).
    
    linewidths : scalar or array_like, optional, default: None
        The linewidth of the marker edges. Note: The default *edgecolors*
        is 'face'. You may want to change this as well.
        If *None*, defaults to rcParams ``lines.linewidth``.
    
    edgecolors : color or sequence of color, optional, default: 'face'
        The edge color of the marker. Possible values:
    
        - 'face': The edge color will always be the same as the face color.
        - 'none': No patch boundary will be drawn.
        - A matplotib color.
    
        For non-filled markers, the *edgecolors* kwarg is ignored and
        forced to 'face' internally.
    
    Returns
    -------
    paths : `~matplotlib.collections.PathCollection`
    
    Other Parameters
    ----------------
    **kwargs : `~matplotlib.collections.Collection` properties
    
    See Also
    --------
    plot : To plot scatter plots when markers are identical in size and
        color.
    
    Notes
    -----
    
    * The `.plot` function will be faster for scatterplots where markers
      don't vary in size or color.
    
    * Any or all of *x*, *y*, *s*, and *c* may be masked arrays, in which
      case all masks will be combined and only unmasked points will be
      plotted.
    
    * Fundamentally, scatter works with 1-D arrays; *x*, *y*, *s*, and *c*
      may be input as 2-D arrays, but within scatter they will be
      flattened. The exception is *c*, which will be flattened only if its
      size matches the size of *x* and *y*.
    
    .. note::
        In addition to the above described arguments, this function can take a
        **data** keyword argument. If such a **data** argument is given, the
        following arguments are replaced by **data[<arg>]**:
    
        * All arguments with the following names: 'c', 'color', 'edgecolors', 'facecolor', 'facecolors', 'linewidths', 's', 'x', 'y'.
    
        Objects passed as **data** must support item access (``data[<arg>]``) and
        membership test (``<arg> in data``).


