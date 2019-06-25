%define major 6
%define libxi %mklibname xi %{major}
%define devname %mklibname xi -d

%global optflags %{optflags} -O3

Summary:	X Input Extension Library
Name:		libxi
Version:	1.7.10
Release:	1
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

%description
X Input Extension Library.

%package -n %{libxi}
Summary:	X Input Extension Library
Group:		Development/X11
Provides:	%{name} = %{EVRD}

%description -n %{libxi}
X Input Extension Library.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libxi} = %{version}-%{release}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Development files for %{name}.

%prep
%autosetup -n libXi-%{version} -p1

%build
%configure \
	--disable-static

%make_build

%install
%make_install

%files -n %{libxi}
%{_libdir}/libXi.so.%{major}*

%files -n %{devname}
%{_libdir}/libXi.so
%{_libdir}/pkgconfig/xi.pc
%{_includedir}/X11/extensions/*.h
%{_datadir}/doc/libXi/*
%{_mandir}/man3/X*
