# libxi is used by wine and steam
%ifarch %{x86_64}
%bcond_without compat32
%else
%bcond_with compat32
%endif

%define major 6
%define libxi %mklibname xi %{major}
%define devname %mklibname xi -d

%if %{with compat32}
%define lib32xi libxi%{major}
%define dev32name libxi-devel
%endif

# Disabling LTO is a workaround for 32-bit gcc wrongfully
# omitting symbols. Not visible at build time, but building
# wine against a gcc LTO-ed version barfs.
# No harm done because we manually add -flto for the 64-bit
# build.
%global _disable_lto 1

Summary:	X Input Extension Library
Name:		libxi
Version:	1.8
Release:	2
License:	MIT
Group:		Development/X11
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXi-%{version}.tar.bz2
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	pkgconfig(xproto)
BuildRequires:	pkgconfig(xorg-macros)
# necessary for building the man pages
BuildRequires:	xmlto
BuildRequires:	asciidoc
BuildRequires:	docbook-dtd412-xml
%if %{with compat32}
BuildRequires:	libc6
BuildRequires:	devel(libX11)
BuildRequires:	devel(libXext)
BuildRequires:	devel(libXfixes)
BuildRequires:	devel(libxcb)
BuildRequires:	devel(libXau)
BuildRequires:	devel(libXdmcp)
%endif

%description
X Input Extension Library.

%package -n %{libxi}
Summary:	X Input Extension Library
Group:		Development/X11

%description -n %{libxi}
X Input Extension Library.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libxi} = %{version}-%{release}

%description -n %{devname}
Development files for %{name}.

%if %{with compat32}
%package -n %{lib32xi}
Summary:	X Input Extension Library (32-bit)
Group:		Development/X11

%description -n %{lib32xi}
X Input Extension Library.

%package -n %{dev32name}
Summary:	Development files for %{name} (32-bit)
Group:		Development/X11
Requires:	%{devname} = %{version}-%{release}
Requires:	%{lib32xi} = %{version}-%{release}

%description -n %{dev32name}
Development files for %{name}.
%endif

%prep
%autosetup -n libXi-%{version} -p1
export CONFIGURE_TOP="$(pwd)"
%if %{with compat32}
mkdir build32
cd build32
%configure32
cd ..
%endif
mkdir build
cd build
CFLAGS="%{optflags} -flto" LDFLAGS="%{build_ldflags} -flto" %configure

%build
%if %{with compat32}
%make_build -C build32
%endif
%make_build -C build

%install
%if %{with compat32}
%make_install -C build32
%endif
%make_install -C build

%files -n %{libxi}
%{_libdir}/libXi.so.%{major}*

%files -n %{devname}
%{_libdir}/libXi.so
%{_libdir}/pkgconfig/xi.pc
%{_includedir}/X11/extensions/*.h
%{_datadir}/doc/libXi/*
%doc %{_mandir}/man3/X*

%if %{with compat32}
%files -n %{lib32xi}
%{_prefix}/lib/libXi.so.%{major}*

%files -n %{dev32name}
%{_prefix}/lib/libXi.so
%{_prefix}/lib/pkgconfig/xi.pc
%endif
