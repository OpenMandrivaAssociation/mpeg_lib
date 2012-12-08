%define major	1
%define libname %mklibname bmpeg %{major}
%define devname %mklibname bmpeg -d

Summary:	Mpeg library
Name:		mpeg_lib
Version:	1.3.1
Release:	21
License:	GPL
Group:		System/Libraries
URL:		http://starship.python.net/~gward/mpeglib/
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
Obsoletes:	%{libname}-devel < 1.3.1-21

%description	-n %{devname}
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
%doc README CHANGES
%{_libdir}/libbmpeg.so.%{major}*

%files -n %{devname}
%doc doc/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/*


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.1-18mdv2011.0
+ Revision: 666489
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.1-17mdv2011.0
+ Revision: 606661
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.1-16mdv2010.1
+ Revision: 521150
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.3.1-15mdv2010.0
+ Revision: 426168
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.3.1-14mdv2009.0
+ Revision: 223319
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 1.3.1-13mdv2008.1
+ Revision: 179084
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Sep 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.1-12mdv2008.0
+ Revision: 89952
- rebuild

* Tue Jun 19 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.3.1-11mdv2008.0
+ Revision: 41251
- Import mpeg_lib



* Sun Jun 18 2006 Götz Waschk <waschk@mandriva.org> 1.3.1-11mdv2007.0
- Rebuild

* Tue Oct 05 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.3.1-10mdk
- reupload since it was removed from repositery despite still being used by
  gimp-1.2

* Wed May 12 2004 Stew Benedict <sbenedict@mandrakesoft.com> 1.3.1-9mdk
- reconstruct last build since -8mdk src.rpm disappeared

* Thu May 06 2004 Stew Benedict <sbenedict@mandrakesoft.com> 1.3.1-8mdk
- ldconfig -> /sbin/ldconfig in %%install

* Tue Sep  2 2003 Abel Cheung <deaddog@deaddog.org> 1.3.1-7mdk
- mklibname
- parallel make is broken

* Tue Jul 22 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 1.3.1-6mdk
- cosmetics
- rm -rf $RPM_BUILD_ROOT at the beginning of %%install

* Tue Jul  9 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.3.1-5mdk
- Patch2: Fix some idiotic bad casts int <-> pointer
- rpmlint fixes: hardcoded-library-path

* Sat Nov  3 2001 Jeff Garzik <jgarzik@mandrakesoft.com> 1.3.1-4mdk
- fix broken ia64 -fPIC change
- add URL tag

* Thu Oct 18 2001 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.3.1-3mdk
- make it -fpic aware for ia64

* Thu Oct 11 2001 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.3.1-2mdk
- provides libbmpeg

* Tue Aug 07 2001 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.3.1-1mdk
- libify
- clean spec

* Mon Jul 16 2001 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.3.1-11mdk
- add so link

* Thu Jul  5 2001 Matthias Badaire <mbadaire@mandrakesoft.com> 1.3.1-10mdk
- ia64 adaptation

* Tue Jun 19 2001 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.3.1-9mdk
- spec cleaning

* Mon Oct  2 2000 Vincent Saugey <vince@mandrakesoft.com> 1.3.1-8mdk
- Correct typo fault in description tag

* Mon Oct  2 2000 Vincent Saugey <vince@mandrakesoft.com> 1.3.1-7mdk
- Adding requires flag to devel package

* Tue Aug 22 2000 Vincent Saugey <vince@mandrakesoft.com> 1.3.1-6mdk
- Correct a broken link (Thx to Stefan van der Eijk) 

* Mon Aug 21 2000 Vincent Saugey <vince@mandrakesoft.com> 1.3.1-5mdk
- add soname
- rename lib, no more confict with kdemultimedia

* Mon Aug 21 2000 Vincent Saugey <vince@mandrakesoft.com> 1.3.1-4mdk
- BM, macros
- split documentation

* Sun Jun 04 2000 David BAUDENS <baudens@mandrakesoft.com> 1.3.1-3mdk
- Fix %%doc
- Fix description of devel package
- Remove unnecessary %%post
- Remove french Description and Summary
- Use %%{_tmppath} for BuildRoot

* Thu May 04 2000 dam's <damien@mandrakesoft.com> 1.3.1-2mdk
- build mpeg_lib and mpeg_lib-devel

* Thu Mar 30 2000 dam's <damien@mandrakesoft.com> 1.3.1-1mdk
- Build Release.

* Sun Nov 07 1999 John Buswell <johnb@mandrakesoft.com>
- Build Release

* Tue Jul 13 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- fix url and source path

* Tue Jul 13 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- fix french translation

* Tue Jul 6 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- new library needed for gimp
- adaptation to Mandrake
- includes fixed
