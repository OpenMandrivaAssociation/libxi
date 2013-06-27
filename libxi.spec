%define major 6
%define libxi %mklibname xi %{major}
%define devname %mklibname xi -d

Summary:	X Input Extension Library
Name:		libxi
Version:	1.7.1
Release:	2
License:	MIT
Group:		Development/X11
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXi-%{version}.tar.bz2
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	pkgconfig(xproto)
BuildRequires:	x11-util-macros
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
Requires:	%{libxi} = %{version}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Development files for %{name}.

%prep
%setup -q -n libXi-%{version}

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

%files -n %{libxi}
%{_libdir}/libXi.so.%{major}*

%files -n %{devname}
%{_libdir}/libXi.so
%{_libdir}/pkgconfig/xi.pc
%{_includedir}/X11/extensions/*.h
%{_datadir}/doc/libXi/*
%{_mandir}/man3/X*

