Summary:	bdftopcf application - convert X font from BDF to PCF
Summary(pl.UTF-8):	Aplikacja bdftopcf - konwersja fontów X z BDF do PCF
Name:		xorg-app-bdftopcf
Version:	1.1
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/bdftopcf-%{version}.tar.bz2
# Source0-md5:	2a455d3c02390597feb9cefb3fe97a45
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-util-util-macros >= 1.8
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
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/bdftopcf
%{_mandir}/man1/bdftopcf.1*
