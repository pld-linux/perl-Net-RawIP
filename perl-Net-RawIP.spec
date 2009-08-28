#
# Conditional build:
%bcond_with	tests	# perform "make test" (uses network!)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	RawIP
Summary:	Net::RawIP perl module
Summary(pl.UTF-8):	Moduł perla Net::RawIP
Name:		perl-Net-RawIP
Version:	0.25
Release:	1
Epoch:		1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a99f461e20e7894154f64729a4652448
BuildRequires:	libpcap-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-libnet
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::RawIP Perl extension to manipulate raw IP packets.

%description -l pl.UTF-8
Net::RawIP - wsparcie do manipulacji surowymi pakietami IP.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Net/RawIP.pm
%dir %{perl_vendorarch}/auto/Net/RawIP
%{perl_vendorarch}/auto/Net/RawIP/RawIP.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Net/RawIP/RawIP.so
%{perl_vendorarch}/auto/Net/RawIP/autosplit.ix
%dir %{perl_vendorarch}/Net/RawIP
%{perl_vendorarch}/Net/RawIP/*.pm
%{_mandir}/man?/*
