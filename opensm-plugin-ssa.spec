Summary:	SSA plugin library (libopensmssa) for OpenSM
Summary(pl.UTF-8):	Biblioteka wtyczki SSA (libopensmssa) dla OpenSM
Name:		opensm-plugin-ssa
Version:	0.0.9
Release:	4
License:	BSD or GPL v2
Group:		Libraries
Source0:	https://www.openfabrics.org/downloads/management/ssa/libopensmssa-%{version}.tar.gz
# Source0-md5:	316dd88c1330e9131d031b2e1f80b40e
Patch0:		libopensmssa-link.patch
Patch1:		gcc10.patch
URL:		https://www.openfabrics.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.2
BuildRequires:	libibumad-devel >= 1.3.10
BuildRequires:	libibverbs-devel >= 1.1.8
BuildRequires:	librdmacm-devel >= 1.0.21
BuildRequires:	libtool >= 2:2
BuildRequires:	opensm-devel >= 3.3.19
BuildRequires:	pkgconfig
Requires:	glib2 >= 1:2.2
Requires:	libibumad >= 1.3.10
Requires:	libibverbs >= 1.1.8
Requires:	librdmacm >= 1.0.21
Requires:	opensm-libs >= 3.3.19
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SSA plugin library (libopensmssa) for OpenSM.

%description -l pl.UTF-8
Biblioteka wtyczki SSA (libopensmssa) dla OpenSM.

%prep
%setup -q -n libopensmssa-%{version}
%patch -P0 -p1
%patch -P1 -p1

%build
%{__libtoolize}
%{__aclocal} -I config
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	GSTACK=/usr/bin/gstack \
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
%{_mandir}/man7/opensmssa.7*
