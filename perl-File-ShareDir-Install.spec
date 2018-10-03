#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	ShareDir-Install
Summary:	File::ShareDir::Install - Install shared files
Summary(pl.UTF-8):	File::ShareDir::Install - instalowanie współdzielonych plików
Name:		perl-File-ShareDir-Install
Version:	0.13
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/File/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5eabd44a5d7d84bf2e8e502491226287
URL:		https://metacpan.org/release/File-ShareDir-Install
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.11
BuildRequires:	perl-Module-Build-Tiny >= 0.034
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Install shared files.

%description -l pl.UTF-8
Instalowanie współdzielonych plików.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/File/ShareDir
%{perl_vendorlib}/File/ShareDir/Install.pm
%{_mandir}/man3/File::ShareDir::Install.3pm*
