#
# Conditional build:
%bcond_without	static_libs # don't build static libraries
#
Summary:	Common Computer Science data structures and algorithms to use in C projects
Summary(pl.UTF-8):   Popularne struktury danych i algorytmy informatyczne do używania w programach w C
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

%description -l pl.UTF-8
Zbiór popularnych struktur danych i algorytmów informatycznych, które
można wykorzystywać w projektach w C.

%package devel
Summary:	Header files for c-algorithms library
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki c-algorithms
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for c-algorithms library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki c-algorithms.

%package static
Summary:	Static c-algorithms library
Summary(pl.UTF-8):   Statyczna biblioteka c-algorithms
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static c-algorithms library.

%description static -l pl.UTF-8
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
