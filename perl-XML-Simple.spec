%define upstream_name 	 XML-Simple
%define upstream_version 2.18

Name: 		perl-%{upstream_name}
Version: 	%perl_convert_version %{upstream_version}
Release: 	%mkrel 2

Summary:	Easy API to maintain XML (esp config files)
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
Buildrequires:	perl(XML::SAX)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
XML::Simple is a trivial perl API to manipulate XML.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
