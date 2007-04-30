%define libxi %mklibname xi 6
Name: libxi
Summary:  X Input Extension Library
Version: 1.0.4
Release: %mkrel 1
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXi-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxext-devel >= 1.0.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

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

%package -n %{libxi}-devel
Summary: Development files for %{name}
Group: Development/X11

Requires: %{libxi} = %{version}
Requires: x11-proto-devel >= 1.0.0
Provides: libxi-devel = %{version}-%{release}

Conflicts: libxorg-x11-devel < 7.0

%description -n %{libxi}-devel
Development files for %{name}

%files -n %{libxi}-devel
%defattr(-,root,root)
%{_libdir}/libXi.so
%{_libdir}/libXi.la
%{_libdir}/pkgconfig/xi.pc
%{_mandir}/man3/X*.3x.bz2

#-----------------------------------------------------------

%package -n %{libxi}-static-devel
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{libxi}-devel = %{version}
Provides: libxi-static-devel = %{version}-%{release}

Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{libxi}-static-devel
Static development files for %{name}

%files -n %{libxi}-static-devel
%defattr(-,root,root)
%{_libdir}/libXi.a

#-----------------------------------------------------------

%prep
%setup -q -n libXi-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -n %{libxi}
%defattr(-,root,root)
%{_libdir}/libXi.so.6
%{_libdir}/libXi.so.6.0.0


