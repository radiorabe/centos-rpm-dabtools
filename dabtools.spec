%define _gh_ref 67123c5b164412915ab9c00f890bcd4826e55bfc

Name:     dabtools

Version:  master
Release:  1
Summary:  DAB/DAB+ software for RTL-SDR dongles including ETI stream recording
License:  GPLv3+
URL:      https://github.com/Opendigitalradio/dabtools
Source0:  https://github.com/Opendigitalradio/dabtools/archive/%{_gh_ref}.tar.gz#/%{name}-%{_gh_ref}.tar.gz
Patch0:   dabtools-makefile-usb.patch

BuildRequires: gcc
BuildRequires: fftw-devel
BuildRequires: rtl-sdr-devel
BuildRequires: libusb-devel

%description
dabtools is work-in-progress set of tools for reception, recording and playback of
DAB and DAB+ digital radio broadcasts. This build does not currently support the
Psion Wavefinder USB DAB tuner but should support any SDR tuner supported by the
RTL-SDR project.


%prep
%setup -q -n %{name}-%{_gh_ref}
%patch0


%build
make -C src/


%install
install -d %{buildroot}/usr/bin/
install src/dab2eti %{buildroot}/usr/bin/
install src/eti2mpa %{buildroot}/usr/bin/


%files
%doc README.md COPYING TODO.md
%{_bindir}/dab2eti
%{_bindir}/eti2mpa
