import yaml
import base64

def linux(conf):
    linux_art = r"""
.____    .__                     
|    |   |__| ____  __ _____  ___
|    |   |  |/    \|  |  \  \/  /
|    |___|  |   |  \  |  />    < 
|_______ \__|___|  /____//__/\_ \
        \/       \/            \/
    """
    print(linux_art)
    print("----------------------------")

    raw_cmd = ""
    for host in conf['linux']:
        hostname = host['hostname']
        user = host['user']
        pw = host['pass']
        cmd = host['cmd']

        print(f"Host: {hostname}")
        print(f"User: {user}")
        print(f"Password: {pw}")
        print(f"cmd: {cmd}")

        ssh_cmd = f"sshpass -p \'{pw}\' ssh {user}@{hostname} \'{cmd}\'"
        print(f"ssh_cmd: {ssh_cmd}")
        raw_cmd += ssh_cmd + ";"

        print("----------------------------")

    # Base64 encode the raw command
    b64 = base64.b64encode(raw_cmd.encode("utf-8")).decode("utf-8")
    enc_cmd = "echo " + b64 + " | base64 -d | bash"

    print("Raw:")
    print(raw_cmd)
    print("Encoded:")
    print(enc_cmd)

def win(conf):
    win_art = r"""
 __      __.__            .___                   
/  \    /  \__| ____    __| _/______  _  ________
\   \/\/   /  |/    \  / __ |/  _ \ \/ \/ /  ___/
 \        /|  |   |  \/ /_/ (  <_> )     /\___ \ 
  \__/\  / |__|___|  /\____ |\____/ \/\_//____  >
       \/          \/      \/                 \/ 
    """
    print(win_art)
    print("----------------------------")
    for host in conf['windows']:
        hostname = host['hostname']
        user = host['user']
        pw = host['pass']
        cmd = host['cmd']

        print(f"Host: {hostname}")
        print(f"User: {user}")
        print(f"Password: {pw}")
        print(f"cmd: {cmd}")
        print("----------------------------")

def main():
    conf_path = "example.yml"
    with open(conf_path, 'r') as file:
        conf = yaml.safe_load(file)
    
    # Linux
    linux(conf)

    # Windows
    win(conf)

if __name__=="__main__":
    main()