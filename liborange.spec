%define major		0
%define libname		%mklibname orange %major
%define develname	%mklibname orange -d

Summary:	Tool to extract CAB files from installers
Name:		liborange
Version:	0.4
Release:	%{mkrel 2}
# Note: linked against LGPL library libgsf
License:	MIT
Group:		Archiving/Other 
Source0:	http://downloads.sourceforge.net/synce/%{name}-%{version}.tar.gz
Patch0:		liborange-0.3.2-underlink.patch
URL:		http://synce.sourceforge.net/
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	libdynamite-devel
BuildRequires:	libsynce-devel
BuildRequires:	unshield-devel
BuildRequires:	libgsf-devel

%description
Liborange is a tool and library to extract CAB files from self-
extracting installers.

%package -n orange
Summary:	Tool to extract CAB files from installers
Group:		Archiving/Other

%description -n orange
Orange is a tool to extract CAB files from self-extracting installers.

%package -n %{libname}
Summary:	Shared library for %{name}
Group:		System/Libraries

%description -n %{libname}
Liborange is a tool and library to extract CAB files from self-
extracting installers. This package contains the shared library.

%package -n %{develname}
Summary:	Development headers for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	orange-devel < %{version}-%{release}
Obsoletes:	%{mklibname orange 0 -d} < %{version}-%{release}

%description -n %{develname}
Liborange is a tool and library to extract CAB files from self-
extracting installers. This package contains the development headers.

%prep
%setup -q
%patch0 -p1 -b .underlink

%build
%configure2_5x --with-libgsf
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n orange
%defattr(-,root,root)
%doc ChangeLog LICENSE TODO
%{_bindir}/*
%{_mandir}/man1/orange.1*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/%{name}.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc ChangeLog LICENSE TODO
%{_includedir}/%{name}*.h
%{_libdir}/%{name}.so
%{_libdir}/%{name}.*a
%{_libdir}/pkgconfig/%{name}.pc



%changelog
* Sun Sep 13 2009 Thierry Vignaud <tv@mandriva.org> 0.4-2mdv2010.0
+ Revision: 438730
- rebuild

* Wed Jan 14 2009 Adam Williamson <awilliamson@mandriva.org> 0.4-1mdv2009.1
+ Revision: 329273
- new release 0.4

* Thu Jul 17 2008 Adam Williamson <awilliamson@mandriva.org> 0.3.2-2mdv2009.0
+ Revision: 237816
- import liborange


