%define major 6
%define libxi %mklibname xi %major
%define libxi_devel %mklibname xi -d
%define libxi_static_devel %mklibname xi -d -s

Name: libxi
Summary:  X Input Extension Library
Version: 1.4.3
Release: %mkrel 1
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXi-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root

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

#-----------------------------------------------------------

%package -n %{libxi}
Summary:  X Input Extension Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libxi}
X Input Extension Library

#-----------------------------------------------------------

%package -n %{libxi_devel}
Summary: Development files for %{name}
Group: Development/X11

Requires: %{libxi} = %{version}
Requires: x11-proto-devel >= 7.5
Provides: libxi-devel = %{version}-%{release}
Obsoletes: %mklibname xi 6 -d

Conflicts: libxorg-x11-devel < 7.0
Conflicts: x11-proto-devel < 7.5

%description -n %{libxi_devel}
Development files for %{name}

%files -n %{libxi_devel}
%defattr(-,root,root)
%{_libdir}/libXi.so
%{_libdir}/libXi.la
%{_libdir}/pkgconfig/xi.pc
%{_includedir}/X11/extensions/*.h
%{_mandir}/man3/X*
%{_datadir}/doc/libXi/doc/*
%{_datadir}/doc/libXi/specs/*

#-----------------------------------------------------------

%package -n %{libxi_static_devel}
Summary: Static development files for %{name}
Group: Development/X11
Requires:  %{libxi_devel} = %{version}-%{release}
Provides:  libxi-static-devel = %{version}-%{release}
Obsoletes: %mklibname xi 6 -d -s

Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{libxi_static_devel}
Static development files for %{name}

%files -n %{libxi_static_devel}
%defattr(-,root,root)
%{_libdir}/libXi.a

#-----------------------------------------------------------

%prep
%setup -q -n libXi-%{version}

%build
%configure2_5x

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -p /sbin/ldconfig
%endif

%files -n %{libxi}
%defattr(-,root,root)
%{_libdir}/libXi.so.%{major}*

