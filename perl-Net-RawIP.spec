%include	/usr/lib/rpm/macros.perl
Summary:	Net-RawIP perl module
Summary(pl):	Modu³ perla Net-RawIP
Name:		perl-Net-RawIP
Version:	0.09d
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/Net-RawIP-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-libnet
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net-RawIP Perl extension to manipulate raw IP packets.

%description -l pl
Net-RawIP - wsparcie do manipulacji surowymi pakietami IP.

%prep
%setup -q -n Net-RawIP-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/*
%{_mandir}/man?/*
