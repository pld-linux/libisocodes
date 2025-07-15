Summary:	Library to access iso-codes data and translations
Summary(pl.UTF-8):	Biblioteka dostępu do danych i tłumaczeń iso-codes
Name:		libisocodes
Version:	1.2.2
Release:	4
License:	GPL v3+
Group:		Libraries
Source0:	http://pkg-isocodes.alioth.debian.org/downloads/%{name}-%{version}.tar.xz
# Source0-md5:	889f6f9b7fa2289ecbc7ecd28db1bdbd
URL:		http://pkg-isocodes.alioth.debian.org/
BuildRequires:	gettext-tools >= 0.18
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libgee-devel >= 0.8
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	vala >= 2:0.16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library can be used to easily access XML data of the iso-codes
package. It will provide an abstraction layer to handle both the
version 3 and the upcoming version 4 of iso-codes. Moreover, all
available translations can be used as well.

This library makes use of the GObject introspection features, so that
it is accessible from a variety of programming languages, for example
C, Vala, Ruby, Python, Perl, Lua, JavaScript, PHP and many more.

%description -l pl.UTF-8
Ta biblioteka pozwala na łatwy dostęp do danych XML pakietu iso-codes.
Zapewnia warstwę abstrakcji do obsługi wersji 3, a także nadchodzącej
wersji 4 pakietu iso-codes. Co więcej, można używać wszystkich
dostępnych tłumaczeń.

Biblioteka wykorzystuje możliwości GObject introspection, dzięki czemu
jest dostępna z wielu języków programowania, jak C, Vala, Ruby,
Python, Perl, Lua, JavaScript, PHP i inne.

%package devel
Summary:	Header files for libisocodes library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libisocodes
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 2.0
Requires:	libgee-devel >= 0.8
Requires:	libxml2-devel >= 2.0

%description devel
Header files for libisocodes library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libisocodes.

%package static
Summary:	Static libisocodes library
Summary(pl.UTF-8):	Statyczna biblioteka libisocodes
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libisocodes library.

%description static -l pl.UTF-8
Statyczna biblioteka libisocodes.

%package -n vala-libisocodes
Summary:	libisocodes API for Vala language
Summary(pl.UTF-8):	API libisocodes dla języka Vala
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
BuildArch:	noarch

%description -n vala-libisocodes
libisocodes API for Vala language.

%description -n vala-libisocodes -l pl.UTF-8
API libisocodes dla języka Vala.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_libdir}/libisocodes.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libisocodes.so.1
%{_libdir}/girepository-1.0/libisocodes-%{version}.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libisocodes.so
%{_datadir}/gir-1.0/libisocodes-%{version}.gir
%{_includedir}/libisocodes.h
%{_pkgconfigdir}/libisocodes.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libisocodes.a

%files -n vala-libisocodes
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/libisocodes.vapi
