import os
import subprocess


def run_encrypt(data):
    env = os.environ.copy()
    env['password'] = '1234456'
    proc = subprocess.Popen(
        ['openssl', 'enc', '-des3', '-pass', 'env:password'],
        env=env,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE)
    proc.stdin.write(data)
    proc.stdin.flush()  # Ensure that the child gets input
    return proc


def run_hash(input_stdin):
    return subprocess.Popen(
        ['openssl', 'dgst', '-whirlpool', '-binary'],
        stdin=input_stdin,
        stdout=subprocess.PIPE
    )


encrypt_procs = []
hash_procs = []
for _ in range(3):
    data = os.urandom(10)
    encrypt_proc = run_encrypt(data)
    encrypt_procs.append(encrypt_proc)
    hash_proc = run_hash(encrypt_proc.stdout)
    hash_procs.append(hash_proc)

for proc in encrypt_procs:
    out, _ = proc.communicate()
    # _ is None
    print(f"encrypt_proc out: {out[-10:]}")
    assert proc.returncode == 0

for proc in hash_procs:
    out, _ = proc.communicate(timeout=1)
    print(f"hash_proc out: {out[-10:]}")


"""
# TODO
1. proc.stdin.flush是什么操作？
2. 为什么单独运行 openssl enc -des3 -pass env:password结束后会一直卡着？
3. 两个子进程几乎同时运行， 后者在等前者的输入， 是什么机制使得后者进行IO等待?
4. communicate的机制， 大概是向stdin输入字符数据， 然后从stdout中读取数据，
   最后等待进程结束
"""
