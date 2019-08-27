Name:           wayfire
Version:        0.2
Release:        0
Summary:        wayfire
Group:          User Interface/X
License:        MIT
URL:            https://github.com/WayfireWM/wayfire
Source0:        https://github.com/WayfireWM/wayfire/archive/master.tar.gz

BuildRequires:  asciidoc
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  meson
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(glm)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(threads)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  wlroots-devel >= 0.6
BuildRequires:  pkgconfig(wf-config)
BuildRequires:  pkgconfig(libinotify)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
Requires:       cairo
Requires:       wf-config
Requires:       glm
Requires:       libjpg

%description
wayfire

%prep
%autosetup -n %{name}-master
mkdir %{_target_platform}

%build
%meson -Dwerror=false
%meson_build

%install
%meson_install

%files

%changelog
* Thu Aug 27 2019 Daniel Kutka <dano.kutka@gmail.com> - 0.2-0
- Initial commit

