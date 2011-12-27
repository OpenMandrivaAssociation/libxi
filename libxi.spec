%define major 6
%define libxi %mklibname xi %{major}
%define develname %mklibname xi -d

Name: libxi
Summary:  X Input Extension Library
Version: 1.5.0
Release: 1
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXi-%{version}.tar.bz2

BuildRequires: libx11-devel >= 1.3
BuildRequires: libxext-devel >= 1.1
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
Provides: %{name} = %{version}

%description -n %{libxi}
X Input Extension Library

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11

Requires: %{libxi} = %{version}
Provides: libxi-devel = %{version}-%{release}
Obsoletes: %{_lib}xi6-devel
Obsoletes: %{_lib}xi-static-devel
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
%{_datadir}/doc/*.xml
%{_mandir}/man3/X*

