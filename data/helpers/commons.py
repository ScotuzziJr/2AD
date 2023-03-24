from ..models import Distro, Desktop, Kernel

def get_all_distros(session):
    return session.query(Distro).all()

def get_distro_by_name(session, distro_name):
    return session.query(Distro).filter_by(name=distro_name).first()

def get_all_desktops(session):
    return session.query(Desktop).all()

def get_desktop_by_name(session, desktop_name):
    return session.query(Desktop).filter_by(name=desktop_name).first()

def get_all_kernels(session):
    return session.query(Kernel).all()

def get_kernel_by_name(session, kernel_name):
    return session.query(Kernel).filter_by(name=kernel_name).first()

def recreate_database(base, db):
    base.metadata.drop_all(db)
    base.metadata.create_all(db)

def add_distro(session, distro_info):
    distro = Distro(
        name=distro_info["name"],
        description=distro_info["description"],
        based_on=distro_info["based_on"],
        desktop=distro_info["desktop"]["name"],
        kernel=distro_info["kernel"]["name"],
        latest_version=distro_info["latest_version"],
        website=distro_info["website"]
    )

    session.add(distro)
    session.commit()

def add_desktop(session, desktop_info):
    desktop = Desktop(
        name=desktop_info["name"],
        latest_version=desktop_info["latest_version"],
    )

    session.add(desktop)
    session.commit()


def add_kernel(session, kernel_info):
    kernel = Kernel(
        name=kernel_info["name"],
        latest_version=kernel_info["latest_version"]
    )

    session.add(kernel)
    session.commit()

def populate_db(session):
    desktop = {
        "name": "GNOME",
        "latest_version": "43"
    }

    if not session.query(Desktop).filter_by(name=desktop["name"]).first():
        add_desktop(session, desktop)

    kernel = {
        "name": "Linux",
        "latest_version": "6.2.8"
    }

    if not session.query(Kernel).filter_by(name=kernel["name"]).first():
        add_kernel(session, kernel)

    distro = {
        "name": "Ubuntu",
        "description": "Ubuntu is a complete desktop Linux operating system, freely available with both community and professional support. The Ubuntu community is built on the ideas enshrined in the Ubuntu Manifesto: that software should be available free of charge, that software tools should be usable by people in their local language and despite any disabilities, and that people should have the freedom to customise and alter their software in whatever way they see fit. 'Ubuntu' is an ancient African word, meaning 'humanity to others'. The Ubuntu distribution brings the spirit of Ubuntu to the software world.",
        "based_on": "Debian",
        "desktop": desktop,
        "kernel": kernel,
        "latest_version": "22.04",
        "website": "https://ubuntu.com/"
    }

    if not session.query(Distro).filter_by(name=distro["name"]).first():
        add_distro(session, distro)

    desktop = {
        "name": "Cinammon",
        "latest_version": "5.6.7"
    }

    if not session.query(Desktop).filter_by(name=desktop["name"]).first():
        add_desktop(session, desktop)

    kernel = {
        "name": "Linux",
        "latest_version": "6.2.8"
    }

    if not session.query(Kernel).filter_by(name=kernel["name"]).first():
        add_kernel(session, kernel)

    distro = {
        "name": "Linux Mint",
        "description": "Linux Mint is an Ubuntu-based distribution whose goal is to provide a classic desktop experience with many convenient, custom tools and optional out-of-the-box multimedia support. It also adds a custom desktop and menus, several unique configuration tools, and a web-based package installation interface. Linux Mint is compatible with Ubuntu software repositories. Besides its Ubuntu-based flavour, the project also produces a separate 'Debian' edition (called LMDE), based on the latest stable Debian version.",
        "based_on": "Ubuntu",
        "desktop": desktop,
        "kernel": kernel,
        "latest_version": "21.1",
        "website": "https://linuxmint.com/"
    }

    if not session.query(Distro).filter_by(name=distro["name"]).first():
        add_distro(session, distro)

    desktop = {
        "name": "GNOME",
        "latest_version": "43"
    }

    if not session.query(Desktop).filter_by(name=desktop["name"]).first():
        add_desktop(session, desktop)

    kernel = {
        "name": "Linux",
        "latest_version": "6.2.8"
    }

    if not session.query(Kernel).filter_by(name=kernel["name"]).first():
        add_kernel(session, kernel)

    distro = {
        "name": "Debian",
        "description": "The Debian Project is an association of individuals who have made common cause to create a free operating system. This operating system is called Debian. Debian systems currently use the Linux kernel. Linux is a completely free piece of software started by Linus Torvalds and supported by thousands of programmers worldwide. Of course, the thing that people want is application software: programs to help them get what they want to do done, from editing documents to running a business to playing games to writing more software. Debian comes with over 50,000 packages (precompiled software that is bundled up in a nice format for easy installation on your machine) - all of it free. It's a bit like a tower. At the base is the kernel. On top of that are all the basic tools. Next is all the software that you run on the computer. At the top of the tower is Debian -- carefully organizing and fitting everything so it all works together.",
        "based_on": "",
        "desktop": desktop,
        "kernel": kernel,
        "latest_version": "11.6",
        "website": "https://www.debian.org/"
    }

    if not session.query(Distro).filter_by(name=distro["name"]).first():
        add_distro(session, distro)

    desktop = {
        "name": "GNOME",
        "latest_version": "43"
    }

    if not session.query(Desktop).filter_by(name=desktop["name"]).first():
        add_desktop(session, desktop)

    kernel = {
        "name": "Linux",
        "latest_version": "6.2.8"
    }

    if not session.query(Kernel).filter_by(name=kernel["name"]).first():
        add_kernel(session, kernel)

    distro = {
        "name": "Fedora",
        "description": "Fedora Linux (formerly Fedora, formerly Fedora Core) is a Linux distribution developed by the community-supported Fedora Project and owned by Red Hat. Fedora Linux contains software distributed under a free and open-source license and aims to be on the leading edge of such technologies. Fedora has a reputation for focusing on innovation, integrating new technologies early on and working closely with upstream Linux communities. The default desktop in Fedora Linux is the GNOME desktop environment and the default interface is the GNOME Shell. Other desktop environments, including KDE, Xfce, LXDE, MATE and Cinnamon, are available. The Fedora project also distributes custom variations of Fedora called Fedora spins. These are built with specific sets of software packages, offering alternative desktop environments or targeting specific interests such as gaming, security, design, scientific computing and robotics.",
        "based_on": "",
        "desktop": desktop,
        "kernel": kernel,
        "latest_version": "37",
        "website": "https://getfedora.org/"
    }

    if not session.query(Distro).filter_by(name=distro["name"]).first():
        add_distro(session, distro)

    desktop = {
        "name": "GNOME",
        "latest_version": "43"
    }

    if not session.query(Desktop).filter_by(name=desktop["name"]).first():
        add_desktop(session, desktop)

    kernel = {
        "name": "Linux",
        "latest_version": "6.2.8"
    }

    if not session.query(Kernel).filter_by(name=kernel["name"]).first():
        add_kernel(session, kernel)

    distro = {
        "name": "Kali Linux",
        "description": "Kali Linux (formerly known as BackTrack) is a Debian-based distribution with a collection of security and forensics tools. It features timely security updates, support for the ARM architecture, a choice of four popular desktop environments, and seamless upgrades to newer versions.",
        "based_on": "Debian",
        "desktop": desktop,
        "kernel": kernel,
        "latest_version": "2023.1",
        "website": "https://www.kali.org/"
    }

    if not session.query(Distro).filter_by(name=distro["name"]).first():
        add_distro(session, distro)
