%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	RawIP
Summary:	Net::RawIP perl module
Summary(pl):	Modu³ perla Net::RawIP
Name:		perl-Net-RawIP
Version:	0.1
Release:	1
Epoch:		1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	libpcap-devel
BuildRequires:	perl >= 5.6.1
BuildRequires:	perl-libnet
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::RawIP Perl extension to manipulate raw IP packets.

%description -l pl
Net::RawIP - wsparcie do manipulacji surowymi pakietami IP.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitearch}/Net/RawIP.pm
%dir %{perl_sitearch}/auto/Net/RawIP
%{perl_sitearch}/auto/Net/RawIP/RawIP.bs
%attr(755,root,root) %{perl_sitearch}/auto/Net/RawIP/RawIP.so
%{perl_sitearch}/auto/Net/RawIP/autosplit.ix
%{_mandir}/man?/*
