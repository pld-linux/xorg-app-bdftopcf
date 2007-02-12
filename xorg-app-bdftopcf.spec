Summary:	bdftopcf application
Summary(pl.UTF-8):   Aplikacja bdftopcf
Name:		xorg-app-bdftopcf
Version:	1.0.0
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/bdftopcf-%{version}.tar.bz2
# Source0-md5:	41f4ac6760ef5e671ba8d4baa7236f12
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXfont-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
bdftopcf application.

%description -l pl.UTF-8
Aplikacja bdftopcf.

%prep
%setup -q -n bdftopcf-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/bdftopcf
%{_mandir}/man1/bdftopcf.1x*
