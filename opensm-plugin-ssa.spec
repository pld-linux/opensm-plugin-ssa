Summary:	SSA plugin library (libopensmssa) for OpenSM
Summary(pl.UTF-8):	Biblioteka wtyczki SSA (libopensmssa) dla OpenSM
Name:		opensm-plugin-ssa
Version:	0.0.8
Release:	1
License:	BSD or GPL v2
Group:		Libraries
Source0:	https://www.openfabrics.org/downloads/management/ssa/libopensmssa-%{version}.tar.gz
# Source0-md5:	7c143fb45fa8476e99f7a385c3e62da6
Patch0:		libopensmssa-link.patch
URL:		https://www.openfabrics.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.2
BuildRequires:	libibumad-devel >= 1.3.10
BuildRequires:	libibverbs-devel >= 1.1.8
BuildRequires:	librdmacm-devel >= 1.0.19
BuildRequires:	libtool
BuildRequires:	opensm-devel >= 3.3.19
BuildRequires:	pkgconfig
Requires:	glib2 >= 1:2.2
Requires:	libibumad >= 1.3.10
Requires:	libibverbs >= 1.1.8
Requires:	librdmacm(ssa) >= 1.0.19
Requires:	opensm-libs >= 3.3.19
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SSA plugin library (libopensmssa) for OpenSM.

%description -l pl.UTF-8
Biblioteka wtyczki SSA (libopensmssa) dla OpenSM.

%prep
%setup -q -n libopensmssa-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I config
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libopensmssa.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README ibssa_core_opts.cfg ssa_release_notes.txt
%attr(755,root,root) %{_libdir}/libopensmssa.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libopensmssa.so.1
%attr(755,root,root) %{_libdir}/libopensmssa.so
