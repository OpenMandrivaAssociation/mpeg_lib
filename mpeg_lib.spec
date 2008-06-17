%define	version	1.3.1

%define major	1
%define libname %mklibname bmpeg %{major}

Summary:	Mpeg library
Name:		mpeg_lib
Version:	%version
Release:	%mkrel 14
License:	GPL
Group:		System/Libraries
URL:		http://starship.python.net/~gward/mpeglib/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

Source0:	ftp://ftp.mni.mcgill.ca/pub/mpeg/%{name}-%{version}.tar.bz2
Patch1:		libmpeg1-1.3.1-debian.diff.bz2
Patch2:		mpeg_lib-1.3.1-bad_cast.patch.bz2 


%description
The MPEG Library is a collection of C routines to decode MPEG movies and dither
them in a variety of colour schemes.  Most of the code in the library comes
directly from the Berkely MPEG player, an X11-specific implementation that
works fine, but suffers from minimal documentation and a lack of modularity.

A front end to the Berkeley decoding engine was developed by Greg Ward at the
Montreal Neurological Institute in May/June 1994 to facilitate the development
of an MPEG player specifically for Silicon Graphics workstations. The decoding
engine together with the MNI front end constitute the MPEG Library.


%package	-n %{libname}
Summary:	Mpeg library
Group:		System/Libraries
Obsoletes:	%{name}
Provides:	%{name} = %{version}-%{release}
Obsoletes:	libbmpeg
Provides:	libbmpeg = %{version}-%{release}

%description	-n %{libname}
The MPEG Library is a collection of C routines to decode MPEG movies and dither
them in a variety of colour schemes.  Most of the code in the library comes
directly from the Berkely MPEG player, an X11-specific implementation that
works fine, but suffers from minimal documentation and a lack of modularity.

A front end to the Berkeley decoding engine was developed by Greg Ward at the
Montreal Neurological Institute in May/June 1994 to facilitate the development
of an MPEG player specifically for Silicon Graphics workstations. The decoding
engine together with the MNI front end constitute the MPEG Library.


%package	-n %{libname}-devel
Summary:	Mpeg library development package
Group:		Development/C
Requires:	%{libname} = %{version}
Obsoletes:	%{name}-devel
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	libbmpeg-devel
Provides:	libbmpeg-devel = %{version}-%{release}

%description	-n %{libname}-devel
The MPEG Library is a collection of C routines to decode MPEG movies and dither
them in a variety of colour schemes.  Most of the code in the library comes
directly from the Berkely MPEG player, an X11-specific implementation that
works fine, but suffers from minimal documentation and a lack of modularity.
 
A front end to the Berkeley decoding engine was developed by Greg Ward at the
Montreal Neurological Institute in May/June 1994 to facilitate the development
of an MPEG player specifically for Silicon Graphics workstations. The decoding
engine together with the MNI front end constitute the MPEG Library.

This package contains static libraries and header files need for development.


%prep
%setup -q
%patch1 -p1
%patch2 -p1 -b .bad_cast

%build
export OPTIMIZE="$RPM_OPT_FLAGS -fPIC"
%configure

make
make shlib

%install
rm -rf $RPM_BUILD_ROOT
install -D -m 644 libmpeg.so.1.3.1 $RPM_BUILD_ROOT%{_libdir}/libbmpeg.so.1.3.1
install -D -m 644 libmpeg.a $RPM_BUILD_ROOT%{_libdir}/libbmpeg.a
install -D -m 644 mpeg.h $RPM_BUILD_ROOT%{_includedir}/bmpeg.h
/sbin/ldconfig -n $RPM_BUILD_ROOT%{_libdir}
ln -s libbmpeg.so.1 $RPM_BUILD_ROOT%{_libdir}/libbmpeg.so

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%doc README CHANGES
%{_libdir}/libbmpeg.so.*


%files -n %{libname}-devel
%defattr(-,root,root)
%doc doc/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/*
