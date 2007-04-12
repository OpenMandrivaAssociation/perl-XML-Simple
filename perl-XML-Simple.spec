%define module 	XML-Simple
%define	name	perl-%{module}
%define version 2.16
%define release %mkrel 1

Summary:	Easy API to maintain XML (esp config files)
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}/
Source:     http://www.cpan.org/modules/by-module/XML/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildRequires:	perl(XML::SAX::Expat)
BuildArch:  	noarch
BuildRoot:  	%{_tmppath}/%{name}-%{version}

%description
XML::Simple is a trivial perl API to manipulate XML.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/XML
%{_mandir}/*/*


