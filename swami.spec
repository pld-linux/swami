Summary:	Sampled Waveforms And Musical Instruments - SoundFont editor
Summary(pl.UTF-8):	Sampled Waveforms And Musical Instruments - edytor fontów dźwiękowych
Name:		swami
Version:	2.2.0
Release:	2
License:	GPL v2
Group:		Applications/Sound
#Source0Download: https://github.com/swami/swami/releases
Source0:	https://github.com/swami/swami/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	d3d5ddffe5227e70e1bf4731b01c3b23
Patch0:		build.patch
URL:		http://www.swamiproject.org/
BuildRequires:	cmake >= 2.6.3
BuildRequires:	fftw3-single-devel >= 3.0
BuildRequires:	fluidsynth-devel >= 2.0
BuildRequires:	glib2-devel >= 1:2.12
BuildRequires:	gtk+2-devel >= 2:2.12
BuildRequires:	gtk-doc
BuildRequires:	libgnomecanvas-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	libinstpatch-devel >= 1.1
Requires:	fftw3-single >= 3.0
Requires:	fluidsynth-devel >= 2.0
Requires:	libswamigui = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Swami (Sampled Waveforms And Musical Instruments) is a SoundFont
editor. SoundFont files are a collection of audio samples and other
data that describe instruments for the purpose of composing music.
SoundFont files do not describe the music itself, but rather the
sounds of the instruments. These instruments can be composed of any
digitally recordable or generated sound. This format provides a
portable and flexible sound synthesis environment that can be
supported in hardware or software.

%description -l pl.UTF-8
Swami (Sampled Waveforms And Musical Instruments - próbkowane krzywe
dźwięku i instrumenty muzyczne) to edytor fontów dźwiękowych. Pliki
fontów dźwiękowych (SoundFont) to zbiór próbek dźwięku i innych danych
opisujących instrumenty na potrzeby komponowania muzyki. Pliki fontów
dźwiękowych nie opisują samej muzyki, ale dźwięki instrumentów.
Instrumenty te mogą być złożone z dowolnych nagranych cyfrowo lub
wygenerowanych dźwięków. Fotmat zapewnia przenośne i elastyczne
środowisko do syntezy dźwięku ze wsparciem sprzętowym lub programowym.

%package -n libswami
Summary:	SWAMI core library
Summary(pl.UTF-8):	Podstawowa biblioteka SWAMI
Group:		Libraries
Requires:	glib2 >= 1:2.12
Requires:	libinstpatch >= 1.1

%description -n libswami
SWAMI core library.

%description -n libswami -l pl.UTF-8
Podstawowa biblioteka SWAMI.

%package -n libswami-devel
Summary:	Header files for SWAMI core library
Summary(pl.UTF-8):	Pliki nagłówkowe podstawowej biblioteki SWAMI
Group:		Development/Libraries
Requires:	libswami = %{version}-%{release}
Requires:	glib2-devel >= 1:2.12
Requires:	libinstpatch-devel >= 1.1

%description -n libswami-devel
Header files for SWAMI core library.

%description -n libswami-devel -l pl.UTF-8
Pliki nagłówkowe podstawowej biblioteki SWAMI.

%package -n libswamigui
Summary:	SWAMI GUI library
Summary(pl.UTF-8):	Biblioteka GUI SWAMI
Group:		X11/Libraries
Requires:	gtk+2-devel >= 2:2.12
Requires:	libgnomecanvas-devel >= 2.0
Requires:	libswami = %{version}-%{release}

%description -n libswamigui
SWAMI GUI library.

%description -n libswamigui -l pl.UTF-8
Biblioteka GUI SWAMI.

%package -n libswamigui-devel
Summary:	Header files for SWAMI GUI library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki GUI SWAMI
Group:		X11/Development/Libraries
Requires:	gtk+2-devel >= 2:2.12
Requires:	libgnomecanvas-devel >= 2.0
Requires:	libswami-devel = %{version}-%{release}
Requires:	libswamigui = %{version}-%{release}

%description -n libswamigui-devel
Header files for SWAMI GUI library.

%description -n libswamigui-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki GUI SWAMI.

%prep
%setup -q
%patch -P0 -p1

%build
install -d build
cd build
%cmake .. \
	-DGTKDOC_ENABLED=ON

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n libswami -p /sbin/ldconfig
%postun	-n libswami -p /sbin/ldconfig

%post	-n libswamigui -p /sbin/ldconfig
%postun	-n libswamigui -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README.md TODO.tasks
%attr(755,root,root) %{_bindir}/swami
%dir %{_libdir}/swami
%attr(755,root,root) %{_libdir}/swami/fftune.so
%attr(755,root,root) %{_libdir}/swami/fftune_gui.so
%attr(755,root,root) %{_libdir}/swami/fluidsynth_gui.so
%attr(755,root,root) %{_libdir}/swami/fluidsynth_plugin.so
%{_datadir}/mime/packages/swami.xml
%{_datadir}/swami
%{_desktopdir}/swami.desktop
%{_iconsdir}/hicolor/48x48/apps/swami.png
%{_iconsdir}/hicolor/scalable/apps/swami.svg

%files -n libswami
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libswami.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libswami.so.1

%files -n libswami-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libswami.so
%dir %{_includedir}/swami
%{_includedir}/swami/libswami

%files -n libswamigui
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libswamigui.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libswamigui.so.1

%files -n libswamigui-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libswamigui.so
%{_includedir}/swami/libswamigui
