Name:           needrestart
Version:        2.11
Release:        1%{?dist}
Summary:        daemon restarter after library updates

Group:          System/Tools
License:        GPLv2
URL:            https://github.com/liske/needrestart
Source0:        https://github.com/liske/needrestart/archive/v%{version}.tar.gz 
#prevent debconf from being required, there is probably a better solution than this
AutoReqProv: no

BuildRequires:  perl perl-ExtUtils-MakeMaker perl-Module-Find perl-Module-ScanDeps perl-Proc-ProcessTable perl-Sort-Naturally perl-TermReadKey perl-parent perl-libintl
Requires:       perl perl-ExtUtils-MakeMaker perl-Module-Find perl-Module-ScanDeps perl-Proc-ProcessTable perl-Sort-Naturally perl-TermReadKey perl-parent perl-libintl

%description
Needrestart can be used to checks whether any daemons need to be restarted after a library update.

%prep
%setup -q

%build
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc /etc/needrestart/conf.d/README.needrestart
/etc/needrestart/hook.d/10-dpkg
/etc/needrestart/hook.d/20-rpm
/etc/needrestart/hook.d/30-pacman
/etc/needrestart/hook.d/90-none
%config /etc/needrestart/needrestart.conf
%config /etc/needrestart/notify.conf
/etc/needrestart/notify.d/200-write 
/etc/needrestart/notify.d/400-notify-send
/etc/needrestart/notify.d/600-mail 
%doc /etc/needrestart/notify.d/README.needrestart

/usr/lib/needrestart
/usr/lib64/perl5/perllocal.pod
/usr/lib64/perl5/vendor_perl/auto/NeedRestart/.packlist
/usr/sbin/needrestart
/usr/share/locale/de/LC_MESSAGES/needrestart-notify.mo
/usr/share/locale/de/LC_MESSAGES/needrestart.mo
/usr/share/perl5/vendor_perl/NeedRestart.pm
/usr/share/perl5/vendor_perl/NeedRestart
/usr/share/polkit-1/actions/net.fiasko-nw.needrestart.policy



%changelog
* Fri Apr 17 2017 Matthias Hörmann <matthias.hoermann@saltation.com> - 2.10-1
- updated to 2.11
* Tue Mar  8 2016 Maximilian Philipps <mphilipps@saltation.de> - 2.7-1
- first created
