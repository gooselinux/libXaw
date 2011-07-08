%define with_compat 0

Summary: X Athena Widget Set
Name: libXaw
Version: 1.0.6
Release: 4.1%{?dist}
License: MIT
URL: http://www.x.org
Group: System Environment/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0: ftp://ftp.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2

BuildRequires: pkgconfig(xproto) pkgconfig(x11) pkgconfig(xt)
BuildRequires: pkgconfig(xmu) pkgconfig(xpm) pkgconfig(xext)
# Required by the configury.
BuildRequires: ed

%description
Xaw is a widget set based on the X Toolkit Intrinsics (Xt) Library.

%if %{with_compat}
%package compat
Summary: X.Org X11 libXaw version 6 compatibility
Group: System Environment/Libraries

%description compat
X.Org X11 libXaw version 6 compatibility
%endif

%package devel
Summary: Development files for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig
Requires: pkgconfig(xproto) pkgconfig(xmu) pkgconfig(xt) pkgconfig(xpm)

%description devel
X.Org X11 libXaw development package

%prep
%setup -q

%build
export CFLAGS="$RPM_OPT_FLAGS -Os"
%configure --disable-xaw8 --disable-static \
%if !%{with_compat}
	   --disable-xaw6
%endif
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING README ChangeLog
%{_libdir}/libXaw.so.7
%{_libdir}/libXaw7.so.7
%{_libdir}/libXaw7.so.7.0.0

%if %{with_compat}
%files compat
%defattr(-,root,root,-)
%{_libdir}/libXaw.so.6
%{_libdir}/libXaw6.so
%{_libdir}/libXaw6.so.6
%{_libdir}/libXaw6.so.6.0.1
%{_libdir}/pkgconfig/xaw6.pc
%endif

%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/X11/Xaw
%doc COPYING
%{_includedir}/X11/Xaw/*.h
# FIXME:  Is this C file really supposed to be here?
%{_includedir}/X11/Xaw/Template.c
%{_libdir}/libXaw.so
%{_libdir}/libXaw7.so
%{_libdir}/pkgconfig/xaw7.pc
%{_mandir}/man3/*.3*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.0.6-4.1
- Rebuilt for RHEL 6

* Thu Aug 13 2009 Parag <paragn@fedoraproject.org> 1.0.6-4
- Merge-review cleanups #226064
- Updated summary, added Requires: pkgconfig
- removed zero length file AUTHORS 

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 23 2009 Adam Jackson <ajax@redhat.com> 1.0.6-2
- Un-require xorg-x11-filesystem
- Remove useless %%dir

* Thu Jul 02 2009 Adam Jackson <ajax@redhat.com> 1.0.6-1
- libXaw 1.0.6

* Thu Jun 11 2009 Adam Jackson <ajax@redhat.com> 1.0.4-5
- Hide libXaw6 behind with_compat, disable by default.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jul 15 2008 Adam Jackson <ajax@redhat.com> 1.0.4-3
- Fix license tag.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.4-2
- Autorebuild for GCC 4.3

* Mon Sep 24 2007 Adam Jackson <ajax@redhat.com> 1.0.4-1
- libXaw 1.0.4

* Thu Sep 06 2007 Adam Jackson <ajax@redhat.com> 1.0.2-10
- Move Xaw6 to a compat package, nothing in the distro needs it.

* Tue Aug 21 2007 Adam Jackson <ajax@redhat.com> - 1.0.2-9
- Rebuild for build id

* Sat Apr 21 2007 Matthias Clasen <mclasen@redhat.com> - 1.0.2-9
- Don't install INSTALL

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.0.2-8.1
- rebuild

* Fri Jul  7 2006 Adam Jackson <ajackson@redhat.com> 1.0.2-8
- Rebuild, brew doesn't pick up buildroot changes fast enough. 

* Wed Jun 28 2006 Adam Jackson <ajackson@redhat.com> 1.0.2-7
- Rebuild for libXt pkgconfig fixes.

* Thu Jun 22 2006 Mike A. Harris <mharris@redhat.com> 1.0.2-6
- Added "Requires: libXpm-devel" to devel subpackage to attempt to fix
  bug (#192040).

* Wed Jun 07 2006 Mike A. Harris <mharris@redhat.com> 1.0.2-5
- Remove package ownership of mandir/libdir/etc.

* Tue Jun 06 2006 Bill Nottingham <notting@redhat.com> 1.0.2-4
- Add "BuildRequires: ed" to fix library sonames

* Mon Jun 05 2006 Mike A. Harris <mharris@redhat.com> 1.0.2-3
- Added "Requires: xorg-x11-proto-devel" to devel package to try to fix
  indirect bug (#192040)

* Mon Jun 05 2006 Mike A. Harris <mharris@redhat.com> 1.0.2-2
- Added "BuildRequires: pkgconfig" for (#193423)
- Replace "makeinstall" with "make install DESTDIR=..."
- Added "BuildRequires: libXt-devel" for (#190169)

* Thu Apr 27 2006 Adam Jackson <ajackson@redhat.com> 1.0.2-1
- Update to 1.0.2

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.0.1-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.0.1-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Jan 18 2006 Mike A. Harris <mharris@redhat.com> 1.0.1-1
- Updated libXaw to version 1.0.1 from X11R7.0

* Fri Dec 16 2005 Mike A. Harris <mharris@redhat.com> 1.0.0-1
- Updated libXaw to version 1.0.0 from X11R7 RC4

* Tue Dec 13 2005 Mike A. Harris <mharris@redhat.com> 0.99.3-1
- Updated libXaw to version 0.99.3 from X11R7 RC3
- Added "Requires(pre): xorg-x11-filesystem >= 0.99.2-3", to ensure
  that /usr/lib/X11 and /usr/include/X11 pre-exist.
- Removed 'x' suffix from manpage directories to match RC3 upstream.

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Sat Nov 12 2005 Mike A. Harris <mharris@redhat.com> 0.99.2-2
- Added libXaw-0.99.2-bug-173027-libtool-sucks.patch to fix bug #173027,
  added 'autoconf' invocation prior to configure, and conditionalized it
  all with with_libtool_sucks_workaround macro.
- Added _smp_mflags to make invocation.
- Use *.h glob in file manifest instead of listing each header individually.

* Fri Nov 11 2005 Mike A. Harris <mharris@redhat.com> 0.99.2-1
- Updated libXaw to version 0.99.2 from X11R7 RC2

* Mon Oct 24 2005 Mike A. Harris <mharris@redhat.com> 0.99.1-1
- Updated libXaw to version 0.99.1 from X11R7 RC1
- Update file manifest to find manpages in "man3x"
- Added {_includedir}/X11/Xaw/Template.c to file manifest

* Thu Sep 29 2005 Mike A. Harris <mharris@redhat.com> 0.99.0-5
- Renamed package to remove xorg-x11 from the name due to unanimous decision
  between developers.
- Use Fedora Extras style BuildRoot tag.
- Disable static library creation by default.
- Add missing defattr to devel subpackage
- Add missing documentation files to doc macro
- Fix all "BuildRequires:" deps with s/xorg-x11-//g

* Wed Aug 25 2005 Mike A. Harris <mharris@redhat.com> 0.99.0-4
- Added dependency on xorg-x11-libXmu-devel to devel subpackage, as libXaw
  headers include libXmu headers directly which caused xkbutils to fail to
  build.

* Wed Aug 24 2005 Mike A. Harris <mharris@redhat.com> 0.99.0-3
- Changed all virtual BuildRequires to the "xorg-x11-" prefixed non-virtual
  package names, as we want xorg-x11 libs to explicitly build against
  X.Org supplied libs, rather than "any implementation", which is what the
  virtual provides is intended for.

* Tue Aug 23 2005 Mike A. Harris <mharris@redhat.com> 0.99.0-2
- Renamed package to prepend "xorg-x11" to the name for consistency with
  the rest of the X11R7 packages.
- Added "Requires: %%{name} = %%{version}-%%{release}" dependency to devel
  subpackage to ensure the devel package matches the installed shared libs.
- Added virtual "Provides: lib<name>" and "Provides: lib<name>-devel" to
  allow applications to use implementation agnostic dependencies.
- Added post/postun scripts which call ldconfig.
- Added Conflicts with XFree86-libs and xorg-x11-libs to runtime package,
  and Conflicts with XFree86-devel and xorg-x11-devel to devel package.

* Mon Aug 22 2005 Mike A. Harris <mharris@redhat.com> 0.99.0-1
- Initial build.
