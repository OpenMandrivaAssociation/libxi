%define major 6
%define libxi %mklibname xi %{major}
%define develname %mklibname xi -d

Name: libxi
Summary:  X Input Extension Library
Version: 1.6.1
Release: 2
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXi-%{version}.tar.bz2

BuildRequires: pkgconfig(x11) >= 1.4.99
BuildRequires: pkgconfig(xext) >= 1.1
BuildRequires: x11-proto-devel >= 7.5
BuildRequires: x11-util-macros >= 1.0.1
# necessary for building the man pages
BuildRequires: xmlto
BuildRequires: asciidoc
BuildRequires: docbook-dtd412-xml

%description
X Input Extension Library

%package -n %{libxi}
Summary:  X Input Extension Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{EVRD}

%description -n %{libxi}
X Input Extension Library

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11

Requires: %{libxi} = %{version}
Provides: libxi-devel = %{EVRD}
Obsoletes: %{_lib}xi6-devel < 1.6.1
Obsoletes: %{_lib}xi-static-devel < 1.6.1
Conflicts: libxorg-x11-devel < 7.0
Conflicts: x11-proto-devel < 7.5

%description -n %{develname}
Development files for %{name}

%prep
%setup -q -n libXi-%{version}

%build
%configure2_5x \
	--disable-static

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%files -n %{libxi}
%{_libdir}/libXi.so.%{major}*

%files -n %{develname}
%{_libdir}/libXi.so
%{_libdir}/pkgconfig/xi.pc
%{_includedir}/X11/extensions/*.h
%{_datadir}/doc/libXi/*
%{_mandir}/man3/X*



%changelog
* Mon May 21 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1.6.1-1
+ Revision: 799746
- Update to 1.6.1

* Thu Mar 29 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1.6.0-1
+ Revision: 788255
- Update to 1.6.0

* Tue Dec 27 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.5.0-1
+ Revision: 745765
- oops
- final files list fix
- fixed files list
- fixed files list
- new version 1.5.0
- disabled static build
- removed .la files
- cleaned up spec

* Sun Jun 19 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.4.3-1
+ Revision: 686009
- update to new version 1.4.3

* Mon Apr 11 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.4.2-1
+ Revision: 652669
- new version 1.4.1

* Wed Jan 26 2011 Thierry Vignaud <tv@mandriva.org> 1.4.1-1
+ Revision: 632909
- new release

* Mon Nov 08 2010 Thierry Vignaud <tv@mandriva.org> 1.4.0-2mdv2011.0
+ Revision: 595113
- move doc from main library into devel subpackage (fix conflict on biarch)

* Mon Nov 08 2010 Thierry Vignaud <tv@mandriva.org> 1.4.0-1mdv2011.0
+ Revision: 594915
- adjust file list
- BuildRequires: docbook-dtd412-xml
- new release

* Wed Aug 04 2010 Thierry Vignaud <tv@mandriva.org> 1.3.2-1mdv2011.0
+ Revision: 565891
- new release

* Mon Aug 02 2010 Thierry Vignaud <tv@mandriva.org> 1.3.1-1mdv2011.0
+ Revision: 565025
- new release

* Mon Nov 09 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.3-1mdv2010.1
+ Revision: 463712
- New version: 1.3

  + Ander Conselvan de Oliveira <ander@mandriva.com>
    - build requires xmlto and asciidoc (needed to build the man pages)

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.2.1-2mdv2010.0
+ Revision: 425926
- rebuild

* Thu Feb 26 2009 Thierry Vignaud <tv@mandriva.org> 1.2.1-1mdv2009.1
+ Revision: 345048
- new release

* Wed Dec 03 2008 Colin Guthrie <cguthrie@mandriva.org> 1.2.0-1mdv2009.1
+ Revision: 309643
- New version: 1.2.0

* Mon Nov 17 2008 Thierry Vignaud <tv@mandriva.org> 1.1.4-1mdv2009.1
+ Revision: 303916
- new release

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.1.3-3mdv2009.0
+ Revision: 223077
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert build requires.

* Mon Jan 14 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.1.3-2mdv2008.1
+ Revision: 151690
- Update BuildRequires and rebuild.

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Oct 09 2007 Thierry Vignaud <tv@mandriva.org> 1.1.3-1mdv2008.1
+ Revision: 96066
- new release

* Wed Aug 01 2007 Colin Guthrie <cguthrie@mandriva.org> 1.1.2-1mdv2008.0
+ Revision: 57471
- New upstream version 1.1.2
- New library policy

* Thu Jul 05 2007 Colin Guthrie <cguthrie@mandriva.org> 1.1.1-1mdv2008.0
+ Revision: 48530
- New upstream version 1.1.1

* Mon Apr 30 2007 Thierry Vignaud <tv@mandriva.org> 1.0.4-2mdv2008.0
+ Revision: 19615
- new release


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 25 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-25 20:17:57 (31598)
- X11R7.1

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 19:54:51 (26912)
- fixed more dependencies

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

