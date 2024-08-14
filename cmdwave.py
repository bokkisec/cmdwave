import yaml

def main():
    with open('example.yml', 'r') as file:
        conf = yaml.safe_load(file)
    
    # Linux
    print("Linux")
    print("--------------")
    for host in conf['linux']:
        print(f"Host: {host['host']}")
        print(f"cmd: {host['cmd']}")
    
    print("--------------")

    # Windows
    print("Windows")
    print("--------------")
    for host in conf['windows']:
        print(f"Host: {host['host']}")
        print(f"cmd: {host['cmd']}")
    print("--------------")

if __name__=="__main__":
    main()