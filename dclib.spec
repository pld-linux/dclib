Summary:	DirectConnect support library for dcgui-qt
Summary(pl):	Biblioteka obs³uguj±ca DirectConenct dla dcgui-qt
Name:		dclib
Version:	0.2rc4
Release:	1
License:	GPL
Group:		X11/Libraries
Source0:	http://download.berlios.de/dcgui/%{name}-%{version}.tar.bz2
#atch0:		%{name}-what.patch
URL:		http://dc.ketelhot.de/
BuildRequires:	qt-devel >= 3.1
BuildRequires:	libxml-devel
BuildRequires:	pth-devel
Requires:	qt >= 3.1
Requires:       libxml
Requires:      	pth
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6

%description
DirectConnect support library for dcgui-qt

%description -l pl
Biblioteka obs³uguj±ca DirectConenct dla dcgui-qt

%package devel
Summary:	Header files for dclib
Summary(pl):	Pliki nag³ówkowe dla dclib
Group:		X11/Development/Libraries
Requires:	dclib = %{version}

%description devel
Header files for dclib

%description devel -l pl
Pliki nag³ówkowe dla dclib

%package static
Summary:      	Static files dclib
Summary(pl):    Pliki statycznie zlinkowanego dclib
Group:          X11/Libraries
Requires:       dclib = %{version}

%description static
Static files dclib

%description static -l pl
Pliki statycznie zlinkowanego dclib


%prep
%setup -q -n %{name}-%{version} 
#patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%preun

%post

%postun

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README ChangeLog
%attr(755,root,root) %{_libdir}/libdc.so*
%{_libdir}/*.la
%{_datadir}/dcgui

%files devel
%defattr(644,root,root,755)
%{_includedir}

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
