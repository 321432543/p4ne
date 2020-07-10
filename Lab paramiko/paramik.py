import paramiko
import time
import pass_config

m_host = pass_config.m_host
m_user = pass_config.m_user
m_pass = pass_config.m_pass


def connect():
    conn = paramiko.SSHClient()
    conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    conn.connect(m_host, username=m_user, password=m_pass, look_for_keys=False, allow_agent=False)
    return conn

def sessio(conn):
    session = conn.invoke_shell()

    session.send("\n")
    session.recv(10000)
    session.send("terminal length 0\n")
    time.sleep(2)

    session.send("\n")
    session.recv(10000)
    session.send("show interfaces\n")
    time.sleep(2)

    out = session.recv(10000)
    return out.decode()

q = sessio(connect())
print(q)
