%define major	1
%define libname %mklibname bmpeg %{major}
%define devname %mklibname bmpeg -d
%define staticname %mklibname bmpeg -d -s

Summary:	Mpeg library
Name:		mpeg_lib
Version:	1.3.1
Release:	26
License:	GPLv2
Group:		System/Libraries
Url:		http://starship.python.net/~gward/mpeglib/
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
Provides:	%{name} = %{version}-%{release}
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

%package	-n %{devname}
Summary:	Mpeg library development package
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	libbmpeg-devel = %{version}-%{release}

%description	-n %{devname}
This package contains header files need for development.

%package	-n %{staticname}
Summary:	Static BMpeg library
Group:		Development/C
Requires:	%{devname} = %{EVRD}

%description	-n %{staticname}
This package contains static libraries of bmpeg.

%prep
%setup -q
%apply_patches

%build
export OPTIMIZE="%{optflags} -fPIC"
%configure

make
make shlib

%install
install -D -m 755 libmpeg.so.1.3.1 %{buildroot}%{_libdir}/libbmpeg.so.1.3.1
install -D -m 644 libmpeg.a %{buildroot}%{_libdir}/libbmpeg.a
install -D -m 644 mpeg.h %{buildroot}%{_includedir}/bmpeg.h
/sbin/ldconfig -n %{buildroot}%{_libdir}
ln -s libbmpeg.so.1 %{buildroot}%{_libdir}/libbmpeg.so

%files -n %{libname}
%{_libdir}/libbmpeg.so.%{major}*

%files -n %{devname}
%doc doc/*
%{_libdir}/*.so
%{_includedir}/*

%files -n %{staticname}
%{_libdir}/*.a
