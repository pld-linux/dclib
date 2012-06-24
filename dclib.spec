%bcond_with	lying	# lie about the H header (always H:1)
Summary:	DirectConnect support library for dcgui-qt
Summary(pl):	Biblioteka obs�uguj�ca DirectConnect dla dcgui-qt
Name:		dclib
Version:	0.3.3
Release:	4
Epoch:		1
License:	GPL
Group:		Libraries
Source0:	http://download.berlios.de/dcgui/%{name}-%{version}.tar.bz2
# Source0-md5:	e25f9afae22341670fa993eb766aaf1e
Patch0:		%{name}-lying_tags.patch
URL:		http://dcgui.berlios.de/
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel > 2.0.0
BuildRequires:	openssl-devel >= 0.9.7d
Requires:	libxml2 > 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DirectConnect support library for dcgui-qt.

%description -l pl
Biblioteka obs�uguj�ca DirectConnect dla dcgui-qt.

%package devel
Summary:	Header files for dclib
Summary(pl):	Pliki nag��wkowe dla dclib
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	bzip2-devel
Requires:	libstdc++-devel
Requires:	libxml2-devel > 2.0.0
Requires:	openssl-devel

%description devel
Header files for dclib.

%description devel -l pl
Pliki nag��wkowe dla dclib.

%package static
Summary:	Static dclib library
Summary(pl):	Statyczna biblioteka dclib
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static dclib library.

%description static -l pl
Statyczna biblioteka dclib.

%prep
%setup -q
%{?with_lying:%patch0 -p1}

%build
cp -f /usr/share/automake/config.sub admin
%configure
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
%doc AUTHORS NEWS README ChangeLog
%attr(755,root,root) %{_libdir}/libdc.so.*.*
%{_datadir}/dclib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/dclib
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
