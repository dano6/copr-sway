%bcond_with check

Name:           meson
Version:        0.50.0
Release:        1%{?dist}
Summary:        High productivity build system

License:        ASL 2.0
URL:            http://mesonbuild.com/
Source0:        https://github.com/mesonbuild/meson/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
Obsoletes:      %{name}-gui < 0.31.0-3

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3-setuptools
%if %{with check}
BuildRequires:  ninja-build
# Various languages
BuildRequires:  gcc
BuildRequires:  libasan
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  gcc-objc
BuildRequires:  gcc-objc++
BuildRequires:  java-devel
BuildRequires:  mono-core mono-devel
BuildRequires:  rust
# Since the build is noarch, we can't use %%ifarch
#%%ifarch %%{ldc_arches}
#BuildRequires:  ldc
#%%endif
# Various libs support
BuildRequires:  boost-devel
BuildRequires:  gtest-devel
BuildRequires:  gmock-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  vala
BuildRequires:  python3-gobject-base
BuildRequires:  wxGTK3-devel
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  gettext
BuildRequires:  gnustep-base-devel
BuildRequires:  %{_bindir}/gnustep-config
BuildRequires:  git-core
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(glib-sharp-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  gtk-doc
BuildRequires:  itstool
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python%{python3_pkgversion}-Cython
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  %{_bindir}/pcap-config
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  llvm-devel
BuildRequires:  cups-devel
%endif
Requires:       ninja-build

%description
Meson is a build system designed to optimize programmer
productivity. It aims to do this by providing simple, out-of-the-box
support for modern software development tools and practices, such as
unit tests, coverage reports, Valgrind, CCache and the like.

%prep
%autosetup -p1
# Remove MPI tests for now because it is complicated to run
rm -rf "test cases/frameworks/17 mpi"
# Macro should not change when we are redefining bindir
sed -i -e "/^%%__meson /s| .*$| %{_bindir}/%{name}|" data/macros.%{name}

%build
%py3_build

%install
%py3_install
install -Dpm0644 data/macros.%{name} %{buildroot}%{rpmmacrodir}/macros.%{name}

%if %{with check}
%check
export MESON_PRINT_TEST_OUTPUT=1
%{__python3} ./run_tests.py
%endif

%files
%license COPYING
%{_bindir}/%{name}
%{python3_sitelib}/mesonbuild/
%{python3_sitelib}/%{name}-*.egg-info/
%{_mandir}/man1/%{name}.1*
%{rpmmacrodir}/macros.%{name}
%dir %{_datadir}/polkit-1
%dir %{_datadir}/polkit-1/actions
%{_datadir}/polkit-1/actions/com.mesonbuild.install.policy

%changelog
* Sun Mar 17 2019 Rafael Gumieri <rafael@gumieri.com> - 0.50.0-1
- Update to 0.50.0

* Sun Oct 21 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.48.1-1
- Update to 0.48.1

* Wed Sep 26 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.48.0-2
- Add missing dependency on setuptools

* Tue Sep 25 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.48.0-1
- Update to 0.48.0

* Sat Aug 25 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.47.2-1
- Update to 0.47.2

* Wed Jul 25 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.47.1-5
- Backport more patches for "feature" option type

* Tue Jul 24 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.47.1-4
- Don't sneak auto-features patch yet

* Tue Jul 24 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.47.1-3
- Macros improvements

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.47.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.47.1-1
- Update to 0.47.1

* Mon Jul 02 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.47.0-1
- Update to 0.47.0

* Thu Jun 28 2018 Miro Hrončok <mhroncok@redhat.com> - 0.46.1-3
- Fix error on Python 3.7 (#1596230)

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 0.46.1-2
- Rebuilt for Python 3.7

* Thu May 17 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.46.1-1
- Update to 0.46.1

* Fri May 04 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.46.0-2
- Backport upstream fixes

* Tue Apr 24 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.46.0-1
- Update to 0.46.0

* Wed Mar 21 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.45.1-1
- Update to 0.45.1

* Sun Mar 04 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.45.0-1
- Update to 0.45.0

* Tue Feb 20 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.44.1-1
- Update to 0.44.1

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.44.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 10 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.44.0-1
- Update to 0.44.0

* Mon Oct 09 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.43.0-1
- Update to 0.43.0

* Tue Sep 12 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.42.1-1
- Update to 0.42.1

* Fri Aug 18 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.42.0-1
- Update to 0.42.0

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.41.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.41.2-1
- Update to 0.41.2

* Tue Jul 18 2017 Kalev Lember <klember@redhat.com> - 0.41.1-3
- Backport various gtk-doc fixes from upstream

* Thu Jul 13 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.41.1-2
- Strip trailing slash from pkg-config files

* Mon Jun 19 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.41.1-1
- Update to 0.41.1

* Tue Jun 13 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.41.0-1
- Update to 0.41.0

* Wed May 31 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.40.1-2
- Don't run ldc tests

* Fri Apr 28 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.40.1-1
- Update to 0.40.1

* Sun Apr 23 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.40.0-1
- Update to 0.40.0

* Thu Apr 13 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.39.1-2
- Exclude ldc for module builds

* Thu Mar 16 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.39.1-1
- Update to 0.39.1

* Mon Mar 06 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.39.0-1
- Update to 0.39.0

* Tue Feb 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.38.1-1
- Update to 0.38.1

* Sun Jan 29 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.38.0-1
- Update to 0.38.0

* Thu Dec 22 2016 Miro Hrončok <mhroncok@redhat.com> - 0.37.1-2
- Rebuild for Python 3.6

* Tue Dec 20 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.37.1-1
- Update to 0.37.1

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.37.0-2
- Rebuild for Python 3.6

* Sun Dec 18 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.37.0-1
- Update to 0.37.0

* Thu Dec 15 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.36.0-4
- Backport more RPM macro fixes (FPC ticket #655)

* Tue Dec 13 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.36.0-3
- Backport fixes to RPM macros

* Sat Dec 03 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.36.0-2
- Print test output during build

* Mon Nov 14 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.36.0-1
- Update to 0.36.0

* Tue Oct 18 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.35.1-1
- Update to 0.35.1 (RHBZ #1385986)

* Tue Oct 11 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.35.0-3
- Backport couple of fixes

* Wed Oct 05 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.35.0-2
- Apply patch to fix FTBFS

* Mon Oct 03 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.35.0-1
- Update to 0.35.0

* Wed Sep 07 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.34.0-2
- Run D test suite

* Wed Sep 07 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.34.0-1
- Update to 0.34.0

* Tue Aug 09 2016 Jon Ciesla <limburgher@gmail.com> - 0.33.0-2
- Obsoletes fix.

* Tue Aug 09 2016 Jon Ciesla <limburgher@gmail.com> - 0.33.0-1
- 0.33.0
- GUI dropped upstream.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.31.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Apr 14 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.31.0-1
- Update to 0.31.0

* Sun Mar 20 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.30.0-1
- Update to 0.30.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 24 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.29.0-1
- Update to 0.29.0

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 0.28.0-2
- Rebuilt for Boost 1.60

* Mon Dec 28 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.28.0-1
- 0.28.0

* Wed Nov 25 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.27.0-1
- 0.27.0

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.26.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Oct 30 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.26.0-2
- Fix rpm macros for using optflags

* Sun Sep 13 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.26.0-1
- 0.26.0

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.25.0-4
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.25.0-2
- rebuild for Boost 1.58

* Sun Jul 12 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.25.0-1
- 0.25.0

* Sat Jul 11 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.24.0-3
- Update URLs
- drop unneded hacks in install section
- enable print test output for tests

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 25 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.24.0-1
- Update to 0.24.0

* Thu May 21 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.23.0-3.20150328git0ba1d54
- Update to latest git

* Thu May 21 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.23.0-3
- Add patch to accept .S files

* Wed Apr 29 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.23.0-2
- Add python3 to Requires (Thanks to Ilya Kyznetsov)

* Tue Mar 31 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.23.0-1
- 0.23.0

* Sat Mar 28 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.22.0-9.20150328git3b49b71
- Update to latest git

* Mon Mar 23 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.22.0-9.20150325git18550fe
- Update to latest git
- Include mesonintrospect

* Mon Mar 23 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.22.0-9.20150322git78d31ca
- Fix filelists for mesongui (python-bytecode-without-source)

* Sun Mar 22 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.22.0-8.20150322git78d31ca
- Enable C# tests

* Sun Mar 22 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.22.0-7.20150322git78d31ca
- update to latest git
- fix tests on arm

* Sat Mar 21 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.22.0-7.20150321gita084a8e
- update to latest git

* Mon Mar 16 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.22.0-7.20150316gitfa2c659
- update to latest git

* Tue Mar 10 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.22.0-7.20150310gitf9f51b1
- today's git snapshot with support for cool GNOME features
- re-enable wxGTK3 tests, package fixed in rawhide

* Thu Feb 26 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.22.0-6.git7581895
- split gui to subpkg
- update to latest snapshot
- enable tests

* Thu Feb 26 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.22.0-5.gitc6dbf98
- Fix packaging style
- Make package noarch

* Mon Feb 23 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.22.0-4.git.c6dbf98
- Use development version

* Sat Feb 21 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.22.0-3
- Add ninja-build to requires

* Thu Jan 22 2015 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.22.0-2
- fix shebang in python files

* Wed Jan 21 2015 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.22.0-1
- Initial package
