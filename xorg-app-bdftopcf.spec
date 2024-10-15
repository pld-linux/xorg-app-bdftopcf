Summary:	bdftopcf application - convert X font from BDF to PCF
Summary(pl.UTF-8):	Aplikacja bdftopcf - konwersja fontów X z BDF do PCF
Name:		xorg-app-bdftopcf
Version:	1.1.2
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/util/bdftopcf-%{version}.tar.xz
# Source0-md5:	c9fc53284f2ac4e23976ff6cde3bddb4
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-proto-fontsproto-devel >= 2.1.3
BuildRequires:	xorg-proto-xproto-devel >= 7.0.22
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
bdftopcf is a font compiler for the X server and font server. Fonts in
Portable Compiled Format can be read by any architecture, although the
file is structured to allow one particular architecture to read them
directly without reformatting. This allows fast reading on the
appropriate machine, but the files are still portable (but read more
slowly) on other machines.

%description -l pl.UTF-8
bdftopcf to kompilator fontów dla serwera X i serwera fontów. Fonty w
formacie PCF (Portable Compiled Format) mogą być odczytywane na
dowolnej architekturze, jednak plik jest tak skonstruowany, że na
określonej architekturze może być czytany bez żadnych przekształceń.
Pozwala to na szybki odczyt na odpowiedniej maszynie, ale pliki są
nadal przenośne na inne maszyny (choć czytane wolniej).

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
%doc AUTHORS COPYING ChangeLog README.md
%attr(755,root,root) %{_bindir}/bdftopcf
%{_mandir}/man1/bdftopcf.1*
