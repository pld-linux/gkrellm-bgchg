Summary:	Backgroud Changer plugin for gkrellm
Summary(pl):	Plugin gkrellm umo¿liwiaj±cy automatyczna zmiane t³a pulpitu
Name:		gkrellmbgchg2
Version:	0.1.4
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.bender-suhl.de/stefan/comp/sources/%{name}-%{version}.tar.gz
# Source0-md5:	4a71cac64f05c578d05af7e19446320a
URL:		http://www.bender-suhl.de/stefan/english/comp/gkrellmbgchg.html
BuildRequires:	gkrellm-devel >= 2.0
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	pkgconfig
Requires:	gkrellm >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GKrellMBgChg is a plugin for GKrellM, which periodically updates the
desktops background image. It is also possible to force an image update by
clicking on the panel or to "hold" the image with the mouse wheel.

%description -l pl
GKrellMBgChg to plugin do GKrellMa, który cyklicznie zmienia t³o pulpitu.

%prep
%setup -q 

%build
# typo - two different variables for optflags
%{__make} \
	CC="%{__cc}" \
	DBGFLAGS="%{rpmcflags}" \
	DGBFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -D gkrellmbgchg.so  $RPM_BUILD_ROOT%{_libdir}/gkrellm2/plugins/gkrellmbgchg.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog TODO
%attr(755,root,root) %{_libdir}/gkrellm2/plugins/gkrellmbgchg.so
