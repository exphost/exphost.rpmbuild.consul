Name:           consul
Version:        1.6.1

%define build_timestamp %(date +"%Y%m%d_%H%M")
Release:        %{build_timestamp}
Summary:        Consul
%undefine _disable_source_fetch

License:        Mozilla Public License 2.0
URL:            https://www.consul.io/
Source0:        https://releases.hashicorp.com/consul/%{?version}/consul_%{?version}_linux_amd64.zip

%description
Consul

%prep
unzip %SOURCE0 

%install
install -d %{?buildroot}/usr/bin
cp consul %{?buildroot}/usr/bin/consul


%clean
rm -rf %{buildroot}

%files
%attr(0755, root, root) /usr/bin/consul
