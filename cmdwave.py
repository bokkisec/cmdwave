import yaml

def main():
    with open('example.yml', 'r') as file:
        conf = yaml.safe_load(file)
    
    # Linux
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
    for host in conf['linux']:
        hostname = host['hostname']
        user = host['user']
        pw = host['pass']
        cmd = host['cmd']

        print(f"Host: {hostname}")
        print(f"User: {user}")
        print(f"Password: {pw}")
        print(f"cmd: {cmd}")
        print("----------------------------")

    # Windows
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

if __name__=="__main__":
    main()