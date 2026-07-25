%define modname	XML-Simple
%define modver 2.25

Summary:	Easy API to maintain XML (esp config files)
Name:		perl-%{modname}
Version:	%{modver}
Release:	5
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://github.com/grantm/xml-simple
Source0:	https://cpan.metacpan.org/authors/id/G/GR/GRANTM/XML-Simple-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl-Test
BuildRequires:	perl-Test-Simple
BuildRequires:	perl(XML::SAX)

%description
XML::Simple is a trivial perl API to manipulate XML.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/XML
%{_mandir}/man3/*


