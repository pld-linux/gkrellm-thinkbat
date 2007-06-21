Summary:	Battery charge metter plugin for gkrellm
Summary(pl.UTF-8):	Wtyczka gkrellma ze stanem baterii
Name:		gkrellm-thinkbat
Version:	0.2.2
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://www.ksp.sk/~rasto/gkrellm-thinkbat/%{name}-%{version}.tar.gz
# Source0-md5:	94be14e34edad900ab04a87f623b2e89
URL:		http://www.thinkwiki.org/wiki/Gkrellm-ThinkBat
BuildRequires:	gkrellm-devel >= 2.0
Requires:	gkrellm >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gkrellm-ThinkBat is meant as a replacement for the default battery
meter in GKrellM.

%description -l pl.UTF-8
gkrellm-ThinkBat zastępuje standardowy monitor baterii w GKrellMie.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -D gkrellm-thinkbat.so $RPM_BUILD_ROOT%{_libdir}/gkrellm2/plugins/gkrellm-thinkbat.so

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/gkrellm2/plugins/gkrellm-thinkbat.so
