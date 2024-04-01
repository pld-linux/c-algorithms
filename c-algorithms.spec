#
# Conditional build:
%bcond_without	static_libs	# static library
#
Summary:	Common Computer Science data structures and algorithms to use in C projects
Summary(pl.UTF-8):	Popularne struktury danych i algorytmy informatyczne do używania w programach w C
Name:		c-algorithms
Version:	1.2.0
Release:	1
License:	ISC
Group:		Libraries
# future versions:
#Source0Download: https://github.com/fragglet/c-algorithms/releases
#Source0:	https://github.com/fragglet/c-algorithms/releases/download/c-algorithms-%{version}/%{name}-%{version}.tar.gz
Source0:	https://downloads.sourceforge.net/c-algorithms/%{name}-%{version}.tar.gz
# Source0-md5:	d104d55ee9c97a2766b0850b44b6e85f
URL:		https://github.com/fragglet/c-algorithms
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	rpm-build >= 4.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Collection of common Computer Science data structures and algorithms
which may be used in C projects.

%description -l pl.UTF-8
Zbiór popularnych struktur danych i algorytmów informatycznych, które
można wykorzystywać w projektach w C.

%package devel
Summary:	Header files for c-algorithms library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki c-algorithms
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for c-algorithms library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki c-algorithms.

%package static
Summary:	Static c-algorithms library
Summary(pl.UTF-8):	Statyczna biblioteka c-algorithms
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static c-algorithms library.

%description static -l pl.UTF-8
Statyczna biblioteka c-algorithms.

%package apidocs
Summary:	API documentation for c-algorithms library
Summary(pl.UTF-8):	Dokumentacja API biblioteki c-algorithms
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for c-algorithms library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki c-algorithms.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static%{!?with_static_libs:=no}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libcalg.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libcalg.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcalg.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcalg.so
%{_includedir}/libcalg-1.0
%{_pkgconfigdir}/libcalg-1.0.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libcalg.a
%endif

%files apidocs
%defattr(644,root,root,755)
%doc doc/html/*.{css,html,png}
