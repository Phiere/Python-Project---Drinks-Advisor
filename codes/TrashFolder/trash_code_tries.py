import re

texte = """
Beta=1 it 1

Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it10.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 40 +/- 0 ; 88 +/- 0 ; 22 +/- 0
 VOI centered at <40,88,22> with radius 0.8 [cm], uncalibrated mean value := 3.76356
 VOI centered at <40,88,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 2.12989
 VOI centered at <40,88,22> with radius 0.8 [cm], nominal value := 4
 VOI centered at <40,88,22> with radius 0.8 [cm], effective volume [cm3] := 2.14769
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it10.img  -x 88 -y 88 -X 0 -Y 0 -r 0.8 -z 22 -U -n 3.0
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it10.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 88 +/- 0 ; 88 +/- 0 ; 22 +/- 0
 VOI centered at <88,88,22> with radius 0.8 [cm], uncalibrated mean value := 2.80326
 VOI centered at <88,88,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 1.8815
 VOI centered at <88,88,22> with radius 0.8 [cm], nominal value := 3
 VOI centered at <88,88,22> with radius 0.8 [cm], effective volume [cm3] := 2.14778
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it10.img  -x 40 -y 40 -X 0 -Y 0 -r 0.8 -z 22 -U -n 2.5
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it10.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 40 +/- 0 ; 40 +/- 0 ; 22 +/- 0
 VOI centered at <40,40,22> with radius 0.8 [cm], uncalibrated mean value := 2.27329
 VOI centered at <40,40,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 1.62099
 VOI centered at <40,40,22> with radius 0.8 [cm], nominal value := 2.5
 VOI centered at <40,40,22> with radius 0.8 [cm], effective volume [cm3] := 2.14761
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it10.img  -x 31 -y 64 -X 0 -Y 0 -r 0.8 -z 22 -U -n 2.0
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it10.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 31 +/- 0 ; 64 +/- 0 ; 22 +/- 0
 VOI centered at <31,64,22> with radius 0.8 [cm], uncalibrated mean value := 1.92375
 VOI centered at <31,64,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 1.26459
 VOI centered at <31,64,22> with radius 0.8 [cm], nominal value := 2
 VOI centered at <31,64,22> with radius 0.8 [cm], effective volume [cm3] := 2.14765
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it10.img  -x 64 -y 97 -X 0 -Y 0 -r 0.8 -z 22 -U -n 1.5
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it10.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 64 +/- 0 ; 97 +/- 0 ; 22 +/- 0
 VOI centered at <64,97,22> with radius 0.8 [cm], uncalibrated mean value := 1.50694
 VOI centered at <64,97,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 1.24457
 VOI centered at <64,97,22> with radius 0.8 [cm], nominal value := 1.5
 VOI centered at <64,97,22> with radius 0.8 [cm], effective volume [cm3] := 2.14774
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it10.img  -x 64 -y 31 -X 0 -Y 0 -r 0.8 -z 22 -U -n 1.3
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it10.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 64 +/- 0 ; 31 +/- 0 ; 22 +/- 0
 VOI centered at <64,31,22> with radius 0.8 [cm], uncalibrated mean value := 1.25816
 VOI centered at <64,31,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 1.13649
 VOI centered at <64,31,22> with radius 0.8 [cm], nominal value := 1.3
 VOI centered at <64,31,22> with radius 0.8 [cm], effective volume [cm3] := 2.14765
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it10.img  -x 88 -y 40 -X 0 -Y 0 -r 0.8 -z 22 -U -n 0.5 -M
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it10.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 88 +/- 0 ; 40 +/- 0 ; 22 +/- 0
 VOI centered at <88,40,22> with radius 0.8 [cm], uncalibrated mean value := 0.411237
 VOI centered at <88,40,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 0.522321
 VOI centered at <88,40,22> with radius 0.8 [cm], nominal value := 0.5
 VOI centered at <88,40,22> with radius 0.8 [cm], effective volume [cm3] := 2.14769
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it10.img  -x 97 -y 64 -X 0 -Y 0 -r 0.8 -z 22 -U -n 0.0 -M
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it10.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 97 +/- 0 ; 64 +/- 0 ; 22 +/- 0
 VOI centered at <97,64,22> with radius 0.8 [cm], uncalibrated mean value := 0.183452
 VOI centered at <97,64,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 0.295685
 VOI centered at <97,64,22> with radius 0.8 [cm], nominal value := 0
 VOI centered at <97,64,22> with radius 0.8 [cm], effective volume [cm3] := 2.14774
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it10.img  -x 64 -y 64 -X 0 -Y 0 -r 0.8 -z 22 -U -n 1.0
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it10.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 64 +/- 0 ; 64 +/- 0 ; 22 +/- 0
 VOI centered at <64,64,22> with radius 0.8 [cm], uncalibrated mean value := 1.03379
 VOI centered at <64,64,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 1.01683
 VOI centered at <64,64,22> with radius 0.8 [cm], nominal value := 1
 VOI centered at <64,64,22> with radius 0.8 [cm], effective volume [cm3] := 2.14769
plesse-costa@biost054:~/Bureau/asim$ 


Beta =1 iteration 2

 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it2.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 40 +/- 0 ; 88 +/- 0 ; 22 +/- 0
 VOI centered at <40,88,22> with radius 0.8 [cm], uncalibrated mean value := 3.79579
 VOI centered at <40,88,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 1.02783
 VOI centered at <40,88,22> with radius 0.8 [cm], nominal value := 4
 VOI centered at <40,88,22> with radius 0.8 [cm], effective volume [cm3] := 2.14769
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it2.img  -x 88 -y 88 -X 0 -Y 0 -r 0.8 -z 22 -U -n 3.0
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it2.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 88 +/- 0 ; 88 +/- 0 ; 22 +/- 0
 VOI centered at <88,88,22> with radius 0.8 [cm], uncalibrated mean value := 2.72513
 VOI centered at <88,88,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 0.816348
 VOI centered at <88,88,22> with radius 0.8 [cm], nominal value := 3
 VOI centered at <88,88,22> with radius 0.8 [cm], effective volume [cm3] := 2.14778
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it2.img  -x 40 -y 40 -X 0 -Y 0 -r 0.8 -z 22 -U -n 2.5
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it2.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 40 +/- 0 ; 40 +/- 0 ; 22 +/- 0
 VOI centered at <40,40,22> with radius 0.8 [cm], uncalibrated mean value := 2.2421
 VOI centered at <40,40,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 0.650435
 VOI centered at <40,40,22> with radius 0.8 [cm], nominal value := 2.5
 VOI centered at <40,40,22> with radius 0.8 [cm], effective volume [cm3] := 2.14761
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it2.img  -x 31 -y 64 -X 0 -Y 0 -r 0.8 -z 22 -U -n 2.0
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it2.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 31 +/- 0 ; 64 +/- 0 ; 22 +/- 0
 VOI centered at <31,64,22> with radius 0.8 [cm], uncalibrated mean value := 1.815
 VOI centered at <31,64,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 0.462656
 VOI centered at <31,64,22> with radius 0.8 [cm], nominal value := 2
 VOI centered at <31,64,22> with radius 0.8 [cm], effective volume [cm3] := 2.14765
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it2.img  -x 64 -y 97 -X 0 -Y 0 -r 0.8 -z 22 -U -n 1.5
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it2.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 64 +/- 0 ; 97 +/- 0 ; 22 +/- 0
 VOI centered at <64,97,22> with radius 0.8 [cm], uncalibrated mean value := 1.39756
 VOI centered at <64,97,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 0.416643
 VOI centered at <64,97,22> with radius 0.8 [cm], nominal value := 1.5
 VOI centered at <64,97,22> with radius 0.8 [cm], effective volume [cm3] := 2.14774
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it2.img  -x 64 -y 31 -X 0 -Y 0 -r 0.8 -z 22 -U -n 1.3
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it2.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 64 +/- 0 ; 31 +/- 0 ; 22 +/- 0
 VOI centered at <64,31,22> with radius 0.8 [cm], uncalibrated mean value := 1.21454
 VOI centered at <64,31,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 0.365345
 VOI centered at <64,31,22> with radius 0.8 [cm], nominal value := 1.3
 VOI centered at <64,31,22> with radius 0.8 [cm], effective volume [cm3] := 2.14765
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it2.img  -x 88 -y 40 -X 0 -Y 0 -r 0.8 -z 22 -U -n 0.5 -M
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it2.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 88 +/- 0 ; 40 +/- 0 ; 22 +/- 0
 VOI centered at <88,40,22> with radius 0.8 [cm], uncalibrated mean value := 0.565508
 VOI centered at <88,40,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 0.184841
 VOI centered at <88,40,22> with radius 0.8 [cm], nominal value := 0.5
 VOI centered at <88,40,22> with radius 0.8 [cm], effective volume [cm3] := 2.14769
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it2.img  -x 97 -y 64 -X 0 -Y 0 -r 0.8 -z 22 -U -n 0.0 -M
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it2.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 97 +/- 0 ; 64 +/- 0 ; 22 +/- 0
 VOI centered at <97,64,22> with radius 0.8 [cm], uncalibrated mean value := 0.366024
 VOI centered at <97,64,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 0.140721
 VOI centered at <97,64,22> with radius 0.8 [cm], nominal value := 0
 VOI centered at <97,64,22> with radius 0.8 [cm], effective volume [cm3] := 2.14774
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it2.img  -x 64 -y 64 -X 0 -Y 0 -r 0.8 -z 22 -U -n 1.0
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it2.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 64 +/- 0 ; 64 +/- 0 ; 22 +/- 0
 VOI centered at <64,64,22> with radius 0.8 [cm], uncalibrated mean value := 1.00767
 VOI centered at <64,64,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 0.30262
 VOI centered at <64,64,22> with radius 0.8 [cm], nominal value := 1
 VOI centered at <64,64,22> with radius 0.8 [cm], effective volume [cm3] := 2.14769
plesse-costa@biost054:~/Bureau/asim/CASToR-recon-cylinder_7_noise-PPGML-huber$ 


Beta =1 it 3

Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it3.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 40 +/- 0 ; 88 +/- 0 ; 22 +/- 0
 VOI centered at <40,88,22> with radius 0.8 [cm], uncalibrated mean value := 3.83798
 VOI centered at <40,88,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 1.28012
 VOI centered at <40,88,22> with radius 0.8 [cm], nominal value := 4
 VOI centered at <40,88,22> with radius 0.8 [cm], effective volume [cm3] := 2.14769
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it3.img  -x 88 -y 88 -X 0 -Y 0 -r 0.8 -z 22 -U -n 3.0
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it3.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 88 +/- 0 ; 88 +/- 0 ; 22 +/- 0
 VOI centered at <88,88,22> with radius 0.8 [cm], uncalibrated mean value := 2.79403
 VOI centered at <88,88,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 1.06851
 VOI centered at <88,88,22> with radius 0.8 [cm], nominal value := 3
 VOI centered at <88,88,22> with radius 0.8 [cm], effective volume [cm3] := 2.14778
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it3.img  -x 40 -y 40 -X 0 -Y 0 -r 0.8 -z 22 -U -n 2.5
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it3.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 40 +/- 0 ; 40 +/- 0 ; 22 +/- 0
 VOI centered at <40,40,22> with radius 0.8 [cm], uncalibrated mean value := 2.29923
 VOI centered at <40,40,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 0.905492
 VOI centered at <40,40,22> with radius 0.8 [cm], nominal value := 2.5
 VOI centered at <40,40,22> with radius 0.8 [cm], effective volume [cm3] := 2.14761
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it3.img  -x 31 -y 64 -X 0 -Y 0 -r 0.8 -z 22 -U -n 2.0
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it3.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 31 +/- 0 ; 64 +/- 0 ; 22 +/- 0
 VOI centered at <31,64,22> with radius 0.8 [cm], uncalibrated mean value := 1.88397
 VOI centered at <31,64,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 0.627455
 VOI centered at <31,64,22> with radius 0.8 [cm], nominal value := 2
 VOI centered at <31,64,22> with radius 0.8 [cm], effective volume [cm3] := 2.14765
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it3.img  -x 64 -y 97 -X 0 -Y 0 -r 0.8 -z 22 -U -n 1.5
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it3.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 64 +/- 0 ; 97 +/- 0 ; 22 +/- 0
 VOI centered at <64,97,22> with radius 0.8 [cm], uncalibrated mean value := 1.45697
 VOI centered at <64,97,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 0.586524
 VOI centered at <64,97,22> with radius 0.8 [cm], nominal value := 1.5
 VOI centered at <64,97,22> with radius 0.8 [cm], effective volume [cm3] := 2.14774
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it3.img  -x 64 -y 31 -X 0 -Y 0 -r 0.8 -z 22 -U -n 1.3
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it3.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 64 +/- 0 ; 31 +/- 0 ; 22 +/- 0
 VOI centered at <64,31,22> with radius 0.8 [cm], uncalibrated mean value := 1.24018
 VOI centered at <64,31,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 0.515677
 VOI centered at <64,31,22> with radius 0.8 [cm], nominal value := 1.3
 VOI centered at <64,31,22> with radius 0.8 [cm], effective volume [cm3] := 2.14765
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it3.img  -x 88 -y 40 -X 0 -Y 0 -r 0.8 -z 22 -U -n 0.5 -M
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it3.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 88 +/- 0 ; 40 +/- 0 ; 22 +/- 0
 VOI centered at <88,40,22> with radius 0.8 [cm], uncalibrated mean value := 0.507754
 VOI centered at <88,40,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 0.235028
 VOI centered at <88,40,22> with radius 0.8 [cm], nominal value := 0.5
 VOI centered at <88,40,22> with radius 0.8 [cm], effective volume [cm3] := 2.14769
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it3.img  -x 97 -y 64 -X 0 -Y 0 -r 0.8 -z 22 -U -n 0.0 -M
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it3.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 97 +/- 0 ; 64 +/- 0 ; 22 +/- 0
 VOI centered at <97,64,22> with radius 0.8 [cm], uncalibrated mean value := 0.299319
 VOI centered at <97,64,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 0.163369
 VOI centered at <97,64,22> with radius 0.8 [cm], nominal value := 0
 VOI centered at <97,64,22> with radius 0.8 [cm], effective volume [cm3] := 2.14774
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it3.img  -x 64 -y 64 -X 0 -Y 0 -r 0.8 -z 22 -U -n 1.0
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it3.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 64 +/- 0 ; 64 +/- 0 ; 22 +/- 0
 VOI centered at <64,64,22> with radius 0.8 [cm], uncalibrated mean value := 1.01763
 VOI centered at <64,64,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 0.427852
 VOI centered at <64,64,22> with radius 0.8 [cm], nominal value := 1
 VOI centered at <64,64,22> with radius 0.8 [cm], effective volume [cm3] := 2.14769
plesse-costa@biost054:~/Bureau/asim/CASToR-recon-cylinder_7_noise-PPGML-huber$ 

beta=1 it 4

Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it4.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 40 +/- 0 ; 88 +/- 0 ; 22 +/- 0
 VOI centered at <40,88,22> with radius 0.8 [cm], uncalibrated mean value := 3.8297
 VOI centered at <40,88,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 1.47804
 VOI centered at <40,88,22> with radius 0.8 [cm], nominal value := 4
 VOI centered at <40,88,22> with radius 0.8 [cm], effective volume [cm3] := 2.14769
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it4.img  -x 88 -y 88 -X 0 -Y 0 -r 0.8 -z 22 -U -n 3.0
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it4.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 88 +/- 0 ; 88 +/- 0 ; 22 +/- 0
 VOI centered at <88,88,22> with radius 0.8 [cm], uncalibrated mean value := 2.80902
 VOI centered at <88,88,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 1.26605
 VOI centered at <88,88,22> with radius 0.8 [cm], nominal value := 3
 VOI centered at <88,88,22> with radius 0.8 [cm], effective volume [cm3] := 2.14778
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it4.img  -x 40 -y 40 -X 0 -Y 0 -r 0.8 -z 22 -U -n 2.5
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it4.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 40 +/- 0 ; 40 +/- 0 ; 22 +/- 0
 VOI centered at <40,40,22> with radius 0.8 [cm], uncalibrated mean value := 2.30711
 VOI centered at <40,40,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 1.09883
 VOI centered at <40,40,22> with radius 0.8 [cm], nominal value := 2.5
 VOI centered at <40,40,22> with radius 0.8 [cm], effective volume [cm3] := 2.14761
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it4.img  -x 31 -y 64 -X 0 -Y 0 -r 0.8 -z 22 -U -n 2.0
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it4.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 31 +/- 0 ; 64 +/- 0 ; 22 +/- 0
 VOI centered at <31,64,22> with radius 0.8 [cm], uncalibrated mean value := 1.90661
 VOI centered at <31,64,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 0.764245
 VOI centered at <31,64,22> with radius 0.8 [cm], nominal value := 2
 VOI centered at <31,64,22> with radius 0.8 [cm], effective volume [cm3] := 2.14765
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it4.img  -x 64 -y 97 -X 0 -Y 0 -r 0.8 -z 22 -U -n 1.5
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it4.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 64 +/- 0 ; 97 +/- 0 ; 22 +/- 0
 VOI centered at <64,97,22> with radius 0.8 [cm], uncalibrated mean value := 1.48309
 VOI centered at <64,97,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 0.728479
 VOI centered at <64,97,22> with radius 0.8 [cm], nominal value := 1.5
 VOI centered at <64,97,22> with radius 0.8 [cm], effective volume [cm3] := 2.14774
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it4.img  -x 64 -y 31 -X 0 -Y 0 -r 0.8 -z 22 -U -n 1.3
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it4.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 64 +/- 0 ; 31 +/- 0 ; 22 +/- 0
 VOI centered at <64,31,22> with radius 0.8 [cm], uncalibrated mean value := 1.25127
 VOI centered at <64,31,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 0.64673
 VOI centered at <64,31,22> with radius 0.8 [cm], nominal value := 1.3
 VOI centered at <64,31,22> with radius 0.8 [cm], effective volume [cm3] := 2.14765
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it4.img  -x 88 -y 40 -X 0 -Y 0 -r 0.8 -z 22 -U -n 0.5 -M
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it4.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 88 +/- 0 ; 40 +/- 0 ; 22 +/- 0
 VOI centered at <88,40,22> with radius 0.8 [cm], uncalibrated mean value := 0.472758
 VOI centered at <88,40,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 0.280826
 VOI centered at <88,40,22> with radius 0.8 [cm], nominal value := 0.5
 VOI centered at <88,40,22> with radius 0.8 [cm], effective volume [cm3] := 2.14769
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it4.img  -x 97 -y 64 -X 0 -Y 0 -r 0.8 -z 22 -U -n 0.0 -M
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it4.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 97 +/- 0 ; 64 +/- 0 ; 22 +/- 0
 VOI centered at <97,64,22> with radius 0.8 [cm], uncalibrated mean value := 0.259445
 VOI centered at <97,64,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 0.18258
 VOI centered at <97,64,22> with radius 0.8 [cm], nominal value := 0
 VOI centered at <97,64,22> with radius 0.8 [cm], effective volume [cm3] := 2.14774
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it4.img  -x 64 -y 64 -X 0 -Y 0 -r 0.8 -z 22 -U -n 1.0
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it4.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 64 +/- 0 ; 64 +/- 0 ; 22 +/- 0
 VOI centered at <64,64,22> with radius 0.8 [cm], uncalibrated mean value := 1.02236
 VOI centered at <64,64,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 0.541473
 VOI centered at <64,64,22> with radius 0.8 [cm], nominal value := 1
 VOI centered at <64,64,22> with radius 0.8 [cm], effective volume [cm3] := 2.14769
plesse-costa@biost054:~/Bureau/asim/CASToR-recon-cylinder_7_noise-PPGML-huber$ 

bera 1 it 5


 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it5.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 40 +/- 0 ; 88 +/- 0 ; 22 +/- 0
 VOI centered at <40,88,22> with radius 0.8 [cm], uncalibrated mean value := 3.81443
 VOI centered at <40,88,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 1.64015
 VOI centered at <40,88,22> with radius 0.8 [cm], nominal value := 4
 VOI centered at <40,88,22> with radius 0.8 [cm], effective volume [cm3] := 2.14769
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it5.img  -x 88 -y 88 -X 0 -Y 0 -r 0.8 -z 22 -U -n 3.0
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it5.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 88 +/- 0 ; 88 +/- 0 ; 22 +/- 0
 VOI centered at <88,88,22> with radius 0.8 [cm], uncalibrated mean value := 2.81124
 VOI centered at <88,88,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 1.42426
 VOI centered at <88,88,22> with radius 0.8 [cm], nominal value := 3
 VOI centered at <88,88,22> with radius 0.8 [cm], effective volume [cm3] := 2.14778
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it5.img  -x 40 -y 40 -X 0 -Y 0 -r 0.8 -z 22 -U -n 2.5
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it5.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 40 +/- 0 ; 40 +/- 0 ; 22 +/- 0
 VOI centered at <40,40,22> with radius 0.8 [cm], uncalibrated mean value := 2.30206
 VOI centered at <40,40,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 1.2453
 VOI centered at <40,40,22> with radius 0.8 [cm], nominal value := 2.5
 VOI centered at <40,40,22> with radius 0.8 [cm], effective volume [cm3] := 2.14761
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it5.img  -x 31 -y 64 -X 0 -Y 0 -r 0.8 -z 22 -U -n 2.0
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it5.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 31 +/- 0 ; 64 +/- 0 ; 22 +/- 0
 VOI centered at <31,64,22> with radius 0.8 [cm], uncalibrated mean value := 1.91444
 VOI centered at <31,64,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 0.880897
 VOI centered at <31,64,22> with radius 0.8 [cm], nominal value := 2
 VOI centered at <31,64,22> with radius 0.8 [cm], effective volume [cm3] := 2.14765
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it5.img  -x 64 -y 97 -X 0 -Y 0 -r 0.8 -z 22 -U -n 1.5
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it5.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 64 +/- 0 ; 97 +/- 0 ; 22 +/- 0
 VOI centered at <64,97,22> with radius 0.8 [cm], uncalibrated mean value := 1.49462
 VOI centered at <64,97,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 0.848463
 VOI centered at <64,97,22> with radius 0.8 [cm], nominal value := 1.5
 VOI centered at <64,97,22> with radius 0.8 [cm], effective volume [cm3] := 2.14774
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it5.img  -x 64 -y 31 -X 0 -Y 0 -r 0.8 -z 22 -U -n 1.3
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it5.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 64 +/- 0 ; 31 +/- 0 ; 22 +/- 0
 VOI centered at <64,31,22> with radius 0.8 [cm], uncalibrated mean value := 1.25597
 VOI centered at <64,31,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 0.760736
 VOI centered at <64,31,22> with radius 0.8 [cm], nominal value := 1.3
 VOI centered at <64,31,22> with radius 0.8 [cm], effective volume [cm3] := 2.14765
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it5.img  -x 88 -y 40 -X 0 -Y 0 -r 0.8 -z 22 -U -n 0.5 -M
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it5.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 88 +/- 0 ; 40 +/- 0 ; 22 +/- 0
 VOI centered at <88,40,22> with radius 0.8 [cm], uncalibrated mean value := 0.450429
 VOI centered at <88,40,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 0.325012
 VOI centered at <88,40,22> with radius 0.8 [cm], nominal value := 0.5
 VOI centered at <88,40,22> with radius 0.8 [cm], effective volume [cm3] := 2.14769
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it5.img  -x 97 -y 64 -X 0 -Y 0 -r 0.8 -z 22 -U -n 0.0 -M
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it5.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 97 +/- 0 ; 64 +/- 0 ; 22 +/- 0
 VOI centered at <97,64,22> with radius 0.8 [cm], uncalibrated mean value := 0.233407
 VOI centered at <97,64,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 0.200935
 VOI centered at <97,64,22> with radius 0.8 [cm], nominal value := 0
 VOI centered at <97,64,22> with radius 0.8 [cm], effective volume [cm3] := 2.14774
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it5.img  -x 64 -y 64 -X 0 -Y 0 -r 0.8 -z 22 -U -n 1.0
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it5.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 64 +/- 0 ; 64 +/- 0 ; 22 +/- 0
 VOI centered at <64,64,22> with radius 0.8 [cm], uncalibrated mean value := 1.02521
 VOI centered at <64,64,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 0.64409
 VOI centered at <64,64,22> with radius 0.8 [cm], nominal value := 1
 VOI centered at <64,64,22> with radius 0.8 [cm], effective volume [cm3] := 2.14769
plesse-costa@biost054:~/Bureau/asim/CASToR-recon-cylinder_7_noise-PPGML-huber$ 

beta 1it 6

 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it6.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 40 +/- 0 ; 88 +/- 0 ; 22 +/- 0
 VOI centered at <40,88,22> with radius 0.8 [cm], uncalibrated mean value := 3.79994
 VOI centered at <40,88,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 1.77451
 VOI centered at <40,88,22> with radius 0.8 [cm], nominal value := 4
 VOI centered at <40,88,22> with radius 0.8 [cm], effective volume [cm3] := 2.14769
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it6.img  -x 88 -y 88 -X 0 -Y 0 -r 0.8 -z 22 -U -n 3.0
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it6.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 88 +/- 0 ; 88 +/- 0 ; 22 +/- 0
 VOI centered at <88,88,22> with radius 0.8 [cm], uncalibrated mean value := 2.81006
 VOI centered at <88,88,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 1.55232
 VOI centered at <88,88,22> with radius 0.8 [cm], nominal value := 3
 VOI centered at <88,88,22> with radius 0.8 [cm], effective volume [cm3] := 2.14778
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it6.img  -x 40 -y 40 -X 0 -Y 0 -r 0.8 -z 22 -U -n 2.5
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it6.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 40 +/- 0 ; 40 +/- 0 ; 22 +/- 0
 VOI centered at <40,40,22> with radius 0.8 [cm], uncalibrated mean value := 2.29435
 VOI centered at <40,40,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 1.35758
 VOI centered at <40,40,22> with radius 0.8 [cm], nominal value := 2.5
 VOI centered at <40,40,22> with radius 0.8 [cm], effective volume [cm3] := 2.14761
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it6.img  -x 31 -y 64 -X 0 -Y 0 -r 0.8 -z 22 -U -n 2.0
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it6.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 31 +/- 0 ; 64 +/- 0 ; 22 +/- 0
 VOI centered at <31,64,22> with radius 0.8 [cm], uncalibrated mean value := 1.91769
 VOI centered at <31,64,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 0.981276
 VOI centered at <31,64,22> with radius 0.8 [cm], nominal value := 2
 VOI centered at <31,64,22> with radius 0.8 [cm], effective volume [cm3] := 2.14765
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it6.img  -x 64 -y 97 -X 0 -Y 0 -r 0.8 -z 22 -U -n 1.5
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it6.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 64 +/- 0 ; 97 +/- 0 ; 22 +/- 0
 VOI centered at <64,97,22> with radius 0.8 [cm], uncalibrated mean value := 1.50018
 VOI centered at <64,97,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 0.951361
 VOI centered at <64,97,22> with radius 0.8 [cm], nominal value := 1.5
 VOI centered at <64,97,22> with radius 0.8 [cm], effective volume [cm3] := 2.14774
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it6.img  -x 64 -y 31 -X 0 -Y 0 -r 0.8 -z 22 -U -n 1.3
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it6.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 64 +/- 0 ; 31 +/- 0 ; 22 +/- 0
 VOI centered at <64,31,22> with radius 0.8 [cm], uncalibrated mean value := 1.25783
 VOI centered at <64,31,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 0.859522
 VOI centered at <64,31,22> with radius 0.8 [cm], nominal value := 1.3
 VOI centered at <64,31,22> with radius 0.8 [cm], effective volume [cm3] := 2.14765
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it6.img  -x 88 -y 40 -X 0 -Y 0 -r 0.8 -z 22 -U -n 0.5 -M
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it6.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 88 +/- 0 ; 40 +/- 0 ; 22 +/- 0
 VOI centered at <88,40,22> with radius 0.8 [cm], uncalibrated mean value := 0.435754
 VOI centered at <88,40,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 0.36827
 VOI centered at <88,40,22> with radius 0.8 [cm], nominal value := 0.5
 VOI centered at <88,40,22> with radius 0.8 [cm], effective volume [cm3] := 2.14769
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it6.img  -x 97 -y 64 -X 0 -Y 0 -r 0.8 -z 22 -U -n 0.0 -M
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it6.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 97 +/- 0 ; 64 +/- 0 ; 22 +/- 0
 VOI centered at <97,64,22> with radius 0.8 [cm], uncalibrated mean value := 0.215642
 VOI centered at <97,64,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 0.21944
 VOI centered at <97,64,22> with radius 0.8 [cm], nominal value := 0
 VOI centered at <97,64,22> with radius 0.8 [cm], effective volume [cm3] := 2.14774
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it6.img  -x 64 -y 64 -X 0 -Y 0 -r 0.8 -z 22 -U -n 1.0
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it6.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 64 +/- 0 ; 64 +/- 0 ; 22 +/- 0
 VOI centered at <64,64,22> with radius 0.8 [cm], uncalibrated mean value := 1.02734
 VOI centered at <64,64,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 0.736415
 VOI centered at <64,64,22> with radius 0.8 [cm], nominal value := 1
 VOI centered at <64,64,22> with radius 0.8 [cm], effective volume [cm3] := 2.14769

beta 1 it 7

Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it7.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 40 +/- 0 ; 88 +/- 0 ; 22 +/- 0
 VOI centered at <40,88,22> with radius 0.8 [cm], uncalibrated mean value := 3.78781
 VOI centered at <40,88,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 1.88668
 VOI centered at <40,88,22> with radius 0.8 [cm], nominal value := 4
 VOI centered at <40,88,22> with radius 0.8 [cm], effective volume [cm3] := 2.14769
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it7.img  -x 88 -y 88 -X 0 -Y 0 -r 0.8 -z 22 -U -n 3.0
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it7.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 88 +/- 0 ; 88 +/- 0 ; 22 +/- 0
 VOI centered at <88,88,22> with radius 0.8 [cm], uncalibrated mean value := 2.80812
 VOI centered at <88,88,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 1.65742
 VOI centered at <88,88,22> with radius 0.8 [cm], nominal value := 3
 VOI centered at <88,88,22> with radius 0.8 [cm], effective volume [cm3] := 2.14778
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it7.img  -x 40 -y 40 -X 0 -Y 0 -r 0.8 -z 22 -U -n 2.5
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it7.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 40 +/- 0 ; 40 +/- 0 ; 22 +/- 0
 VOI centered at <40,40,22> with radius 0.8 [cm], uncalibrated mean value := 2.28715
 VOI centered at <40,40,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 1.44535
 VOI centered at <40,40,22> with radius 0.8 [cm], nominal value := 2.5
 VOI centered at <40,40,22> with radius 0.8 [cm], effective volume [cm3] := 2.14761
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it7.img  -x 31 -y 64 -X 0 -Y 0 -r 0.8 -z 22 -U -n 2.0
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it7.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 31 +/- 0 ; 64 +/- 0 ; 22 +/- 0
 VOI centered at <31,64,22> with radius 0.8 [cm], uncalibrated mean value := 1.91957
 VOI centered at <31,64,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 1.06789
 VOI centered at <31,64,22> with radius 0.8 [cm], nominal value := 2
 VOI centered at <31,64,22> with radius 0.8 [cm], effective volume [cm3] := 2.14765
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it7.img  -x 64 -y 97 -X 0 -Y 0 -r 0.8 -z 22 -U -n 1.5
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it7.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 64 +/- 0 ; 97 +/- 0 ; 22 +/- 0
 VOI centered at <64,97,22> with radius 0.8 [cm], uncalibrated mean value := 1.50322
 VOI centered at <64,97,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 1.04038
 VOI centered at <64,97,22> with radius 0.8 [cm], nominal value := 1.5
 VOI centered at <64,97,22> with radius 0.8 [cm], effective volume [cm3] := 2.14774
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it7.img  -x 64 -y 31 -X 0 -Y 0 -r 0.8 -z 22 -U -n 1.3
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it7.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 64 +/- 0 ; 31 +/- 0 ; 22 +/- 0
 VOI centered at <64,31,22> with radius 0.8 [cm], uncalibrated mean value := 1.25845
 VOI centered at <64,31,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 0.944821
 VOI centered at <64,31,22> with radius 0.8 [cm], nominal value := 1.3
 VOI centered at <64,31,22> with radius 0.8 [cm], effective volume [cm3] := 2.14765
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it7.img  -x 88 -y 40 -X 0 -Y 0 -r 0.8 -z 22 -U -n 0.5 -M
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it7.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 88 +/- 0 ; 40 +/- 0 ; 22 +/- 0
 VOI centered at <88,40,22> with radius 0.8 [cm], uncalibrated mean value := 0.425919
 VOI centered at <88,40,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 0.410316
 VOI centered at <88,40,22> with radius 0.8 [cm], nominal value := 0.5
 VOI centered at <88,40,22> with radius 0.8 [cm], effective volume [cm3] := 2.14769
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it7.img  -x 97 -y 64 -X 0 -Y 0 -r 0.8 -z 22 -U -n 0.0 -M
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it7.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 97 +/- 0 ; 64 +/- 0 ; 22 +/- 0
 VOI centered at <97,64,22> with radius 0.8 [cm], uncalibrated mean value := 0.203218
 VOI centered at <97,64,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 0.23836
 VOI centered at <97,64,22> with radius 0.8 [cm], nominal value := 0
 VOI centered at <97,64,22> with radius 0.8 [cm], effective volume [cm3] := 2.14774
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it7.img  -x 64 -y 64 -X 0 -Y 0 -r 0.8 -z 22 -U -n 1.0
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it7.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 64 +/- 0 ; 64 +/- 0 ; 22 +/- 0
 VOI centered at <64,64,22> with radius 0.8 [cm], uncalibrated mean value := 1.0292
 VOI centered at <64,64,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 0.819188
 VOI centered at <64,64,22> with radius 0.8 [cm], nominal value := 1
 VOI centered at <64,64,22> with radius 0.8 [cm], effective volume [cm3] := 2.14769
plesse-costa@biost054:~/Bureau/asim/CASToR-recon-cylinder_7_noise-PPGML-huber$ 

beta 1 it8
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it8.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 88 +/- 0 ; 88 +/- 0 ; 22 +/- 0
 VOI centered at <88,88,22> with radius 0.8 [cm], uncalibrated mean value := 2.8062
 VOI centered at <88,88,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 1.74485
 VOI centered at <88,88,22> with radius 0.8 [cm], nominal value := 3
 VOI centered at <88,88,22> with radius 0.8 [cm], effective volume [cm3] := 2.14778
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it8.img  -x 40 -y 40 -X 0 -Y 0 -r 0.8 -z 22 -U -n 2.5
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it8.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 40 +/- 0 ; 40 +/- 0 ; 22 +/- 0
 VOI centered at <40,40,22> with radius 0.8 [cm], uncalibrated mean value := 2.28124
 VOI centered at <40,40,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 1.51551
 VOI centered at <40,40,22> with radius 0.8 [cm], nominal value := 2.5
 VOI centered at <40,40,22> with radius 0.8 [cm], effective volume [cm3] := 2.14761
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it8.img  -x 31 -y 64 -X 0 -Y 0 -r 0.8 -z 22 -U -n 2.0
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it8.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 31 +/- 0 ; 64 +/- 0 ; 22 +/- 0
 VOI centered at <31,64,22> with radius 0.8 [cm], uncalibrated mean value := 1.92105
 VOI centered at <31,64,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 1.1428
 VOI centered at <31,64,22> with radius 0.8 [cm], nominal value := 2
 VOI centered at <31,64,22> with radius 0.8 [cm], effective volume [cm3] := 2.14765
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it8.img  -x 64 -y 97 -X 0 -Y 0 -r 0.8 -z 22 -U -n 1.5
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it8.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 64 +/- 0 ; 97 +/- 0 ; 22 +/- 0
 VOI centered at <64,97,22> with radius 0.8 [cm], uncalibrated mean value := 1.50503
 VOI centered at <64,97,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 1.11777
 VOI centered at <64,97,22> with radius 0.8 [cm], nominal value := 1.5
 VOI centered at <64,97,22> with radius 0.8 [cm], effective volume [cm3] := 2.14774
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it8.img  -x 64 -y 31 -X 0 -Y 0 -r 0.8 -z 22 -U -n 1.3
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it8.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 64 +/- 0 ; 31 +/- 0 ; 22 +/- 0
 VOI centered at <64,31,22> with radius 0.8 [cm], uncalibrated mean value := 1.25853
 VOI centered at <64,31,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 1.01835
 VOI centered at <64,31,22> with radius 0.8 [cm], nominal value := 1.3
 VOI centered at <64,31,22> with radius 0.8 [cm], effective volume [cm3] := 2.14765
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it8.img  -x 88 -y 40 -X 0 -Y 0 -r 0.8 -z 22 -U -n 0.5 -M
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it8.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 88 +/- 0 ; 40 +/- 0 ; 22 +/- 0
 VOI centered at <88,40,22> with radius 0.8 [cm], uncalibrated mean value := 0.419216
 VOI centered at <88,40,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 0.450459
 VOI centered at <88,40,22> with radius 0.8 [cm], nominal value := 0.5
 VOI centered at <88,40,22> with radius 0.8 [cm], effective volume [cm3] := 2.14769
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it8.img  -x 97 -y 64 -X 0 -Y 0 -r 0.8 -z 22 -U -n 0.0 -M
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it8.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 97 +/- 0 ; 64 +/- 0 ; 22 +/- 0
 VOI centered at <97,64,22> with radius 0.8 [cm], uncalibrated mean value := 0.194394
 VOI centered at <97,64,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 0.257579
 VOI centered at <97,64,22> with radius 0.8 [cm], nominal value := 0
 VOI centered at <97,64,22> with radius 0.8 [cm], effective volume [cm3] := 2.14774
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it8.img  -x 64 -y 64 -X 0 -Y 0 -r 0.8 -z 22 -U -n 1.0
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it8.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 64 +/- 0 ; 64 +/- 0 ; 22 +/- 0
 VOI centered at <64,64,22> with radius 0.8 [cm], uncalibrated mean value := 1.0309
 VOI centered at <64,64,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 0.893085
 VOI centered at <64,64,22> with radius 0.8 [cm], nominal value := 1
 VOI centered at <64,64,22> with radius 0.8 [cm], effective volume [cm3] := 2.14769
plesse-costa@biost054:~/Bureau/asim/CASToR-recon-cylinder_7_noise-PPGML-huber$ 

beta 1 it 9

 spherical VOI radius: 0.8 cm
 VOI center range: 64 +/- 0 ; 64 +/- 0 ; 22 +/- 0
 VOI centered at <64,64,22> with radius 0.8 [cm], uncalibrated mean value := 1.0309
 VOI centered at <64,64,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 0.893085
 VOI centered at <64,64,22> with radius 0.8 [cm], nominal value := 1
 VOI centered at <64,64,22> with radius 0.8 [cm], effective volume [cm3] := 2.14769
plesse-costa@biost054:~/Bureau/asim/CASToR-recon-cylinder_7_noise-PPGML-huber$ python3 ../voi.py
Please enter the image file name: CASToR-recon-cylinder_7_noise-PPGML-huber_it9.img
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it9.img  -x 40 -y 88 -X 0 -Y 0 -r 0.8 -z 22 -U -n 4.0
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it9.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 40 +/- 0 ; 88 +/- 0 ; 22 +/- 0
 VOI centered at <40,88,22> with radius 0.8 [cm], uncalibrated mean value := 3.77001
 VOI centered at <40,88,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 2.06121
 VOI centered at <40,88,22> with radius 0.8 [cm], nominal value := 4
 VOI centered at <40,88,22> with radius 0.8 [cm], effective volume [cm3] := 2.14769
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it9.img  -x 88 -y 88 -X 0 -Y 0 -r 0.8 -z 22 -U -n 3.0
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it9.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 88 +/- 0 ; 88 +/- 0 ; 22 +/- 0
 VOI centered at <88,88,22> with radius 0.8 [cm], uncalibrated mean value := 2.80456
 VOI centered at <88,88,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 1.81854
 VOI centered at <88,88,22> with radius 0.8 [cm], nominal value := 3
 VOI centered at <88,88,22> with radius 0.8 [cm], effective volume [cm3] := 2.14778
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it9.img  -x 40 -y 40 -X 0 -Y 0 -r 0.8 -z 22 -U -n 2.5
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it9.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 40 +/- 0 ; 40 +/- 0 ; 22 +/- 0
 VOI centered at <40,40,22> with radius 0.8 [cm], uncalibrated mean value := 2.2767
 VOI centered at <40,40,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 1.57298
 VOI centered at <40,40,22> with radius 0.8 [cm], nominal value := 2.5
 VOI centered at <40,40,22> with radius 0.8 [cm], effective volume [cm3] := 2.14761
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it9.img  -x 31 -y 64 -X 0 -Y 0 -r 0.8 -z 22 -U -n 2.0
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it9.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 31 +/- 0 ; 64 +/- 0 ; 22 +/- 0
 VOI centered at <31,64,22> with radius 0.8 [cm], uncalibrated mean value := 1.92242
 VOI centered at <31,64,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 1.20786
 VOI centered at <31,64,22> with radius 0.8 [cm], nominal value := 2
 VOI centered at <31,64,22> with radius 0.8 [cm], effective volume [cm3] := 2.14765
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it9.img  -x 64 -y 97 -X 0 -Y 0 -r 0.8 -z 22 -U -n 1.5
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it9.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 64 +/- 0 ; 97 +/- 0 ; 22 +/- 0
 VOI centered at <64,97,22> with radius 0.8 [cm], uncalibrated mean value := 1.50618
 VOI centered at <64,97,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 1.18533
 VOI centered at <64,97,22> with radius 0.8 [cm], nominal value := 1.5
 VOI centered at <64,97,22> with radius 0.8 [cm], effective volume [cm3] := 2.14774
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it9.img  -x 64 -y 31 -X 0 -Y 0 -r 0.8 -z 22 -U -n 1.3
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it9.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 64 +/- 0 ; 31 +/- 0 ; 22 +/- 0
 VOI centered at <64,31,22> with radius 0.8 [cm], uncalibrated mean value := 1.25839
 VOI centered at <64,31,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 1.08174
 VOI centered at <64,31,22> with radius 0.8 [cm], nominal value := 1.3
 VOI centered at <64,31,22> with radius 0.8 [cm], effective volume [cm3] := 2.14765
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it9.img  -x 88 -y 40 -X 0 -Y 0 -r 0.8 -z 22 -U -n 0.5 -M
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it9.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 88 +/- 0 ; 40 +/- 0 ; 22 +/- 0
 VOI centered at <88,40,22> with radius 0.8 [cm], uncalibrated mean value := 0.414556
 VOI centered at <88,40,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 0.487973
 VOI centered at <88,40,22> with radius 0.8 [cm], nominal value := 0.5
 VOI centered at <88,40,22> with radius 0.8 [cm], effective volume [cm3] := 2.14769
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it9.img  -x 97 -y 64 -X 0 -Y 0 -r 0.8 -z 22 -U -n 0.0 -M
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it9.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 97 +/- 0 ; 64 +/- 0 ; 22 +/- 0
 VOI centered at <97,64,22> with radius 0.8 [cm], uncalibrated mean value := 0.188055
 VOI centered at <97,64,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 0.276806
 VOI centered at <97,64,22> with radius 0.8 [cm], nominal value := 0
 VOI centered at <97,64,22> with radius 0.8 [cm], effective volume [cm3] := 2.14774
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it9.img  -x 64 -y 64 -X 0 -Y 0 -r 0.8 -z 22 -U -n 1.0
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it9.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 64 +/- 0 ; 64 +/- 0 ; 22 +/- 0
 VOI centered at <64,64,22> with radius 0.8 [cm], uncalibrated mean value := 1.03244
 VOI centered at <64,64,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 0.958743
 VOI centered at <64,64,22> with radius 0.8 [cm], nominal value := 1
 VOI centered at <64,64,22> with radius 0.8 [cm], effective volume [cm3] := 2.14769

beta 1 it 10 
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it10.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 40 +/- 0 ; 88 +/- 0 ; 22 +/- 0
 VOI centered at <40,88,22> with radius 0.8 [cm], uncalibrated mean value := 3.76356
 VOI centered at <40,88,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 2.12989
 VOI centered at <40,88,22> with radius 0.8 [cm], nominal value := 4
 VOI centered at <40,88,22> with radius 0.8 [cm], effective volume [cm3] := 2.14769
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it10.img  -x 88 -y 88 -X 0 -Y 0 -r 0.8 -z 22 -U -n 3.0
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it10.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 88 +/- 0 ; 88 +/- 0 ; 22 +/- 0
 VOI centered at <88,88,22> with radius 0.8 [cm], uncalibrated mean value := 2.80326
 VOI centered at <88,88,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 1.8815
 VOI centered at <88,88,22> with radius 0.8 [cm], nominal value := 3
 VOI centered at <88,88,22> with radius 0.8 [cm], effective volume [cm3] := 2.14778
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it10.img  -x 40 -y 40 -X 0 -Y 0 -r 0.8 -z 22 -U -n 2.5
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it10.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 40 +/- 0 ; 40 +/- 0 ; 22 +/- 0
 VOI centered at <40,40,22> with radius 0.8 [cm], uncalibrated mean value := 2.27329
 VOI centered at <40,40,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 1.62099
 VOI centered at <40,40,22> with radius 0.8 [cm], nominal value := 2.5
 VOI centered at <40,40,22> with radius 0.8 [cm], effective volume [cm3] := 2.14761
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it10.img  -x 31 -y 64 -X 0 -Y 0 -r 0.8 -z 22 -U -n 2.0
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it10.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 31 +/- 0 ; 64 +/- 0 ; 22 +/- 0
 VOI centered at <31,64,22> with radius 0.8 [cm], uncalibrated mean value := 1.92375
 VOI centered at <31,64,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 1.26459
 VOI centered at <31,64,22> with radius 0.8 [cm], nominal value := 2
 VOI centered at <31,64,22> with radius 0.8 [cm], effective volume [cm3] := 2.14765
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it10.img  -x 64 -y 97 -X 0 -Y 0 -r 0.8 -z 22 -U -n 1.5
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it10.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 64 +/- 0 ; 97 +/- 0 ; 22 +/- 0
 VOI centered at <64,97,22> with radius 0.8 [cm], uncalibrated mean value := 1.50694
 VOI centered at <64,97,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 1.24457
 VOI centered at <64,97,22> with radius 0.8 [cm], nominal value := 1.5
 VOI centered at <64,97,22> with radius 0.8 [cm], effective volume [cm3] := 2.14774
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it10.img  -x 64 -y 31 -X 0 -Y 0 -r 0.8 -z 22 -U -n 1.3
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it10.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 64 +/- 0 ; 31 +/- 0 ; 22 +/- 0
 VOI centered at <64,31,22> with radius 0.8 [cm], uncalibrated mean value := 1.25816
 VOI centered at <64,31,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 1.13649
 VOI centered at <64,31,22> with radius 0.8 [cm], nominal value := 1.3
 VOI centered at <64,31,22> with radius 0.8 [cm], effective volume [cm3] := 2.14765
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it10.img  -x 88 -y 40 -X 0 -Y 0 -r 0.8 -z 22 -U -n 0.5 -M
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it10.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 88 +/- 0 ; 40 +/- 0 ; 22 +/- 0
 VOI centered at <88,40,22> with radius 0.8 [cm], uncalibrated mean value := 0.411237
 VOI centered at <88,40,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 0.522321
 VOI centered at <88,40,22> with radius 0.8 [cm], nominal value := 0.5
 VOI centered at <88,40,22> with radius 0.8 [cm], effective volume [cm3] := 2.14769
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it10.img  -x 97 -y 64 -X 0 -Y 0 -r 0.8 -z 22 -U -n 0.0 -M
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it10.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 97 +/- 0 ; 64 +/- 0 ; 22 +/- 0
 VOI centered at <97,64,22> with radius 0.8 [cm], uncalibrated mean value := 0.183452
 VOI centered at <97,64,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 0.295685
 VOI centered at <97,64,22> with radius 0.8 [cm], nominal value := 0
 VOI centered at <97,64,22> with radius 0.8 [cm], effective volume [cm3] := 2.14774
/biomaps/physics/appli/comtat/ecat_voi_1_9 -i CASToR-recon-cylinder_7_noise-PPGML-huber_it10.img  -x 64 -y 64 -X 0 -Y 0 -r 0.8 -z 22 -U -n 1.0
 Input file: CASToR-recon-cylinder_7_noise-PPGML-huber_it10.img
 Matrix    : 1,1,1,0,0
 Image size: 128 X 128 X 45
 Voxel size: 0.2 cm X 0.2 cm X 0.556 cm
 spherical VOI radius: 0.8 cm
 VOI center range: 64 +/- 0 ; 64 +/- 0 ; 22 +/- 0
 VOI centered at <64,64,22> with radius 0.8 [cm], uncalibrated mean value := 1.03379
 VOI centered at <64,64,22> with radius 0.8 [cm], uncalibrated standard-deviation value := 1.01683
 VOI centered at <64,64,22> with radius 0.8 [cm], nominal value := 1
 VOI centered at <64,64,22> with radius 0.8 [cm], effective volume [cm3] := 2.14769
plesse-costa@biost054:~/Bureau/asim/CASToR-recon-cylinder_7_noise-PPGML-huber$ 




"""

# Utilisation d'une expression régulière pour trouver les nombres après "uncalibrated mean value :="
pattern_mean_value = r"uncalibrated mean value := (\d+\.\d+|\d+)"
pattern_standar_deviation_value = r"uncalibrated standard-deviation value := (\d+\.\d+|\d+)"
pattern_nominal = r"nominal value := (\d+\.\d+|\d+)"
pattern_volume =  r"effective volume \[cm3\] := (\d+\.\d+|\d+)"

resultats_mean = re.findall(pattern_mean_value, texte)
resultats_std = re.findall(pattern_standar_deviation_value, texte)
resultats_nom = re.findall(pattern_nominal, texte)
resultats_vol = re.findall(pattern_volume, texte)

# Convertir les chaînes trouvées en nombres réels
means = [float(num) for num in resultats_mean]
std =  [float(num) for num in resultats_std]
nom = [float(num) for num in resultats_nom]
vol =  [float(num) for num in resultats_vol]

for element in means :
    print(element)

print("oui")
for element in std :
    print(element)
print("oui")
for element in nom :
    print(element)
print("oui")
for element in vol :
    print(element)



