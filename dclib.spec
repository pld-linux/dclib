Summary:	DirectConnect support library for dcgui-qt
Summary(pl):	Biblioteka obs³uguj±ca DirectConnect dla dcgui-qt
Name:		dclib
Version:	0.2rc4
Release:	3
License:	GPL
Group:		X11/Libraries
Source0:	http://download.berlios.de/dcgui/%{name}-%{version}.tar.bz2
URL:		http://dc.ketelhot.de/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel > 2.0.0
BuildRequires:	pth-devel
Requires:	libxml2 > 2.0.0
Requires:	pth
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6

%description
DirectConnect support library for dcgui-qt.

%description -l pl
Biblioteka obs³uguj±ca DirectConnect dla dcgui-qt.

%package devel
Summary:	Header files for dclib
Summary(pl):	Pliki nag³ówkowe dla dclib
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for dclib.

%description devel -l pl
Pliki nag³ówkowe dla dclib.

%package static
Summary:	Static dclib library
Summary(pl):	Statyczna biblioteka dclib
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static dclib library.

%description static -l pl
Statyczna biblioteka dclib.

%prep
%setup -q -n %{name}-%{version} 

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

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
