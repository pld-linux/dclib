%define	_snap	040521
Summary:	DirectConnect support library for dcgui-qt
Summary(pl):	Biblioteka obs³uguj±ca DirectConnect dla dcgui-qt
Name:		dclib
Version:	0.3
Release:	0.%{_snap}.1
License:	GPL
Group:		Libraries
Source0:	http://dcgui.berlios.de/files/dcgui/snapshot/dc-source-alpha-snapshot.tar.gz
# Source0-md5:	f2fd65496a2cc6149038e7b87a398beb
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
Biblioteka obs³uguj±ca DirectConnect dla dcgui-qt.

%package devel
Summary:	Header files for dclib
Summary(pl):	Pliki nag³ówkowe dla dclib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	bzip2-devel
Requires:	libstdc++-devel
Requires:	libxml2-devel > 2.0.0
Requires:	openssl-devel

%description devel
Header files for dclib.

%description devel -l pl
Pliki nag³ówkowe dla dclib.

%package static
Summary:	Static dclib library
Summary(pl):	Statyczna biblioteka dclib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static dclib library.

%description static -l pl
Statyczna biblioteka dclib.

%prep
##%setup -q -n dclib
cd $RPM_BUILD_DIR
if [ -d %{name}-%{version} ]; then
rm -rf %{name}-%{version}
fi
mkdir %{name}-%{version}
cd %{name}-%{version}
tar xfz %{SOURCE0} -C ./

%build
cd $RPM_BUILD_DIR/%{name}-%{version}/dclib
##export UNSERMAKE=/usr/share/unsermake/unsermake
%{__make} -f Makefile.dist
##cp -f /usr/share/automake/config.sub admin
%configure --with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
cd $RPM_BUILD_DIR/%{name}-%{version}/dclib/

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
%{_datadir}/dcgui

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/dclib

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
