%define upstream_name 	 XML-Simple
%define upstream_version 2.18

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Easy API to maintain XML (esp config files)
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(XML::SAX)
BuildArch:	noarch

%description
XML::Simple is a trivial perl API to manipulate XML.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/XML
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 2.180.0-4mdv2012.0
+ Revision: 765853
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 2.180.0-3
+ Revision: 764385
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.180.0-2
+ Revision: 667458
- mass rebuild

* Tue Jul 28 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.180.0-1mdv2011.0
+ Revision: 401852
- rebuild using %%perl_convert_version

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 2.18-4mdv2009.1
+ Revision: 351664
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 2.18-3mdv2009.0
+ Revision: 224664
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 2.18-2mdv2008.1
+ Revision: 180660
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 16 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.18-1mdv2008.0
+ Revision: 64640
- new version

* Mon Aug 06 2007 Funda Wang <fwang@mandriva.org> 2.17-1mdv2008.0
+ Revision: 59416
- New version 2.17


* Thu Dec 14 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.16-1mdv2007.0
+ Revision: 96784
- new version
- Import perl-XML-Simple

* Fri Feb 04 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 2.14-1mdk
- 2.14

* Wed Nov 24 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 2.13-1mdk
- 2.13

* Sat Apr 24 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.12-1mdk
- 2.12

