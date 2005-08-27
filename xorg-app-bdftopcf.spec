Summary:	bdftopcf application
Summary(pl):	Aplikacja bdftopcf
Name:		xorg-app-bdftopcf
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/app/bdftopcf-%{version}.tar.bz2
# Source0-md5:	8f23af1e43ad6bc94e92421a225a69ce
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libXfont-devel
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkgconfig >= 0.19
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
bdftopcf application.

%description -l pl
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
%attr(755,root,wheel) %{_bindir}/bdftopcf
%{_mandir}/man1/*.1*
