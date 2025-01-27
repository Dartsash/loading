import time
import random
import sys

print('Installing by Dartsash')

print('-----------------------------------------------------------------------------')

def progress_bar(task_name, total, prefix='', suffix='', length=40, fill='█'):
    for i in range(total + 1):
        percent = 100 * (i / float(total))
        filled_length = int(length * i // total)
        bar = fill * filled_length + '-' * (length - filled_length)
        sys.stdout.write(f'\r{prefix} |{bar}| {percent:.2f}% {suffix}')
        sys.stdout.flush()
        time.sleep(5 / total)

    sys.stdout.write('\n')

def fake_download():
    print("Starting Pterodactyl installation")
    time.sleep(1)
    print("Downloading required files...")
    time.sleep(0.3)
    progress_bar("Downloading", 100, prefix="Progress", suffix="Complete")
    time.sleep(1)
    print("Configuring environment...")
    time.sleep(0.3)
    progress_bar("Configuring", 50, prefix="Progress", suffix="Complete")
    time.sleep(1)

    print("Finalizing installation...")
    time.sleep(0.1)
    progress_bar("Finalizing", 30, prefix="Progress", suffix="Complete")
    time.sleep(0.3)
    print("Pterodactyl installed successfully!")
    time.sleep(3)
    print("Run panel.dartworld.ru to access the panel.")
    time.sleep(2)

    print("Opening ports and finalizing security settings...")
    progress_bar("Opening Ports", 60, prefix="Progress", suffix="Complete")

    actions = [
        "Importing necessary libraries...",
        "Updating system packages...",
        "Creating config file /etc/ufw/before.rules with new version",
        "Creating config file /etc/ufw/before6.rules with new version.",
        "Creating config file /etc/ufw/after.rules with new version",
        "Creating config file /etc/ufw/after6.rules with new version",
        "Setting up php-common (2:95+ubuntu22.04.1+deb.sury.org+1)...",
        "Setting up php-common (2:95+ubuntu22.04.1+deb.sury.org+1)...",
        "Setting up libhttp-date-perl (6.05-1)...",
        "Setting up php8.3-common (8.3.15-1+ubuntu22.04.1+deb.sury.org+1)...",
        "Setting up php8.3-zip (8.3.15-1+ubuntu22.04.1+deb.sury.org+1)...",
        "Setting up php8.3-mysql (8.3.15-1+ubuntu22.04.1+deb.sury.org+1)...",
        "Setting up php8.3-mbstring (8.3.15-1+ubuntu22.04.1+deb.sury.org+1)...",
        "Setting up php8.3-readline (8.3.15-1+ubuntu22.04.1+deb.sury.org+1)...",
        "Setting up mariadb-client-core-10.6 (1:10.6.18-0ubuntu0.22.04.1)...",
        "Setting up redis-tools (5:6.0.16-1ubuntu1)...",
        "Setting up libgav1-0:amd64 (0.17.0-1build1)...",
        "Setting up libdbd-mysql-perl:amd64 (4.050-5ubuntu0.22.04.1)...",
        "Setting up git (1:2.48.1-0ppa1~ubuntu22.04.1)...",
        "Setting up libavif13:amd64 (0.9.3-3)...",
        "Setting up php8.3-bcmath (8.3.15-1+ubuntu22.04.1+deb.sury.org+1)...",
        "Setting up libhtml-parser-perl:amd64 (3.76-1build2)...",
        "Setting up php8.3-xml (8.3.15-1+ubuntu22.04.1+deb.sury.org+1)...",
        "Setting up php8.3-opcache (8.3.15-1+ubuntu22.04.1+deb.sury.org+1)...",
        "Setting up mariadb-client-10.6 (1:10.6.18-0ubuntu0.22.04.1)...",
        "Setting up rsync (3.2.7-0ubuntu0.22.04.4)...",
        "invoke-rc.d: could not determine current runlevel",
        "invoke-rc.d: policy-rc.d denied execution of start.",
        "Setting up libhttp-message-perl (6.36-1)..."
    ]

    for action in actions:
        print(action)
        time.sleep(random.uniform(0.1, 0.5))

if __name__ == "__main__":
    fake_download()

print('Installing Complete')
time.sleep(3)
