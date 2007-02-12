Summary:	Backgroud Changer plugin for gkrellm
Summary(pl.UTF-8):   Wtyczka gkrellm umożliwiająca automatyczną zmianę tła pulpitu
Name:		gkrellm-bgchg
Version:	0.1.7
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.bender-suhl.de/stefan/comp/sources/gkrellmbgchg2-%{version}.tar.gz
# Source0-md5:	edeeb8960fd0005a472e3bc6ec1c9852
URL:		http://www.bender-suhl.de/stefan/english/comp/gkrellmbgchg.html
BuildRequires:	gkrellm-devel >= 2.0
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	pkgconfig
Requires:	gkrellm >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GKrellMBgChg is a plugin for GKrellM, which periodically updates the
desktops background image. It is also possible to force an image
update by clicking on the panel or to "hold" the image with the mouse
wheel.

%description -l pl.UTF-8
GKrellMBgChg to wtyczka do GKrellMa, która cyklicznie zmienia tło
pulpitu. Umożliwia także wymuszenie uaktualnienia obrazka przez
kliknięcie na panelu albo "przytrzymanie" obrazka kółkiem myszy.

%prep
%setup -q -n gkrellmbgchg2-%{version}

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -fPIC \$(GTK_INCLUDE) \$(GKRELLM_INCLUDE)"

%install
rm -rf $RPM_BUILD_ROOT

install -D gkrellmbgchg.so $RPM_BUILD_ROOT%{_libdir}/gkrellm2/plugins/gkrellmbgchg.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog TODO
%attr(755,root,root) %{_libdir}/gkrellm2/plugins/gkrellmbgchg.so
