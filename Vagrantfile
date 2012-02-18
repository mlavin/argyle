Vagrant::Config.run do |config|
    config.vm.define :"argyle-test" do |config|
        config.vm.box = "lucid32"
        config.vm.network("33.33.33.10")
        config.vm.customize do |vm|
            vm.memory_size = 256
        end
    end
end
