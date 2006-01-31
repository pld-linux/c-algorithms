#
# Conditional build:
%bcond_without	static_libs # don't build static libraries
#
Summary:	Collection of common Computer Science data structures and algorithms which may be used in C projects
#Summary(pl):	-
Name:		c-algorithms
Version:	1.0.0
Release:	0.1
License:	BSD-like
Group:		Libraries
Source0:	http://dl.sourceforge.net/c-algorithms/%{name}-%{version}.tar.gz
# Source0-md5:	3435f8705ff83360b48bfba61decdb7a
URL:		http://c-algorithms.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Collection of common Computer Science data structures and algorithms
which may be used in C projects.

##%description -l pl

%package devel
Summary:	Header files for c-algorithms library
Summary(pl):	Pliki nag³ówkowe biblioteki c-algorithms
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig

%description devel
Header files for c-algorithms library.

%description devel -l pl
Pliki nag³ówkowe biblioteki c-algorithms.

%package static
Summary:	Static c-algorithms library
Summary(pl):	Statyczna biblioteka c-algorithms
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static c-algorithms library.

%description static -l pl
Statyczna biblioteka c-algorithms.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static=%{?with_static_libs:yes}%{!?with_static_libs:no}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/html/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/libcalg-1.0
%{_pkgconfigdir}/*.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif
