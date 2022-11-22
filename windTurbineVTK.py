import vtk
import numpy as np

# def callback_function(caller, timer_event):
# 	assembly.RotateX(1)
# 	renWin.Render() 



# assembly = vtk.vtkAssembly()
# nonMovingfilenames = ["/Users/richardfindlay/Desktop/windTurbine/mesh/non/nacelle.stl", "/Users/richardfindlay/Desktop/windTurbine/mesh/non/tower.stl", 
# 	"/Users/richardfindlay/Desktop/windTurbine/mesh//hub.stl", 
# 	"/Users/richardfindlay/Desktop/windTurbine/mesh//blade1-cap.stl",
# 	"/Users/richardfindlay/Desktop/windTurbine/mesh//blade1-pressureSide1.stl",
# 	"/Users/richardfindlay/Desktop/windTurbine/mesh//blade1-pressureSide2.stl",
# 	"/Users/richardfindlay/Desktop/windTurbine/mesh//blade1-suctionSide1.stl",
# 	"/Users/richardfindlay/Desktop/windTurbine/mesh//blade1-suctionSide2.stl",
# 	"/Users/richardfindlay/Desktop/windTurbine/mesh//blade2-cap.stl",
# 	"/Users/richardfindlay/Desktop/windTurbine/mesh//blade2-pressureSide1.stl",
# 	"/Users/richardfindlay/Desktop/windTurbine/mesh//blade2-pressureSide2.stl",
# 	"/Users/richardfindlay/Desktop/windTurbine/mesh//blade2-suctionSide1.stl",
# 	"/Users/richardfindlay/Desktop/windTurbine/mesh//blade2-suctionSide2.stl",
# 	"/Users/richardfindlay/Desktop/windTurbine/mesh//blade3-cap.stl",
# 	"/Users/richardfindlay/Desktop/windTurbine/mesh//blade3-pressureSide1.stl",
# 	"/Users/richardfindlay/Desktop/windTurbine/mesh//blade3-pressureSide2.stl",
# 	"/Users/richardfindlay/Desktop/windTurbine/mesh//blade3-suctionSide1.stl",
# 	"/Users/richardfindlay/Desktop/windTurbine/mesh//blade3-suctionSide2.stl"
# 	]


# for filename in nonMovingfilenames:
#     stl_reader = vtk.vtkSTLReader()
#     stl_reader.SetFileName(filename)

#     stl_mapper = vtk.vtkPolyDataMapper()
#     stl_mapper.SetInputConnection(stl_reader.GetOutputPort())

#     stl_actor = vtk.vtkActor()
#     if filename == "/Users/richardfindlay/Desktop/windTurbine/mesh/non/nacelle.stl":
#         stl_actor.GetProperty().SetColor(0.86,0.08,0.24)
#     else:
#         stl_actor.GetProperty().SetOpacity(1)
#     stl_actor.SetMapper(stl_mapper)

#     assembly.AddPart(stl_actor)

# ren = vtk.vtkRenderer()
# renWin = vtk.vtkRenderWindow()
# renWin.AddRenderer(ren)
 
# #Create a renderwindowinteractor
# iren = vtk.vtkRenderWindowInteractor()
# iren.SetRenderWindow(renWin)

# ren.AddActor(assembly)
# ren.SetBackground(1,1,1)

# iren.Initialize()
# iren.CreateRepeatingTimer(int(1/560))
# iren.AddObserver("TimerEvent", callback_function)

# # Enable user interface interactor
# # iren.Initialize()
# renWin.Render()
# iren.Start()


######################


def callback_function(caller, timer_event):
	assembly2.RotateWXYZ(1,1,0,0)
	# assembly.RotateZ(0.5)
	# assembly.RotateWXYZ(0.5,0,0,1)
	# stl_actor3.RotateZ(0)
	# stl_reader_tower = vtk.vtkSTLReader()
	# stl_reader_tower.SetFileName("/Users/richardfindlay/Desktop/windTurbine/mesh/NewOrigin_Test/New_Origin_tower_Tower2.stl")

	# stl_mapper_tower = vtk.vtkPolyDataMapper()
	# stl_mapper_tower.SetInputConnection(stl_reader_tower.GetOutputPort())

	# stl_actor_tower = vtk.vtkActor()

	# stl_actor_tower.GetProperty().SetOpacity(1)
	# stl_actor_tower.SetMapper(stl_mapper_tower)

	# centerYAW = stl_actor_tower.GetCenter()


	# # transform = assembly2.GetUserTransform()
	# transform.Translate(centerYAW[0], centerYAW[1], centerYAW[2])
	# transform.RotateWXYZ(1, 0, 1, 0)
	# transform.Translate(-centerYAW[0], -centerYAW[1], -centerYAW[2])




	renWin.Render() 


def callback_function2(caller, timer_event):

	m = 180
	

	# stl_reader_tower = vtk.vtkSTLReader()
	# stl_reader_tower.SetFileName("/Users/richardfindlay/Desktop/windTurbine/mesh/NewOrigin_Test/New_Origin_tower_Tower2.stl")

	# stl_mapper_tower = vtk.vtkPolyDataMapper()
	# stl_mapper_tower.SetInputConnection(stl_reader_tower.GetOutputPort())

	# stl_actor_tower = vtk.vtkActor()

	# stl_actor_tower.GetProperty().SetOpacity(1)
	# stl_actor_tower.SetMapper(stl_mapper_tower)


	# stl_reader_nac = vtk.vtkSTLReader()
	# stl_reader_nac.SetFileName("/Users/richardfindlay/Desktop/windTurbine/mesh/NewOrigin_Test/New_Origin_Nacelle2.stl")



	# centerYAW = stl_actor_tower.GetCenter()


	transform = vtk.vtkTransform()
	transform.Translate(centerYAW[0], centerYAW[1], centerYAW[2])
	transform.RotateWXYZ(m,0,0,1)
	transform.Translate(-centerYAW[0], -centerYAW[1], -centerYAW[2])
	transformFilter=vtk.vtkTransformPolyDataFilter()
	transformFilter.SetTransform(transform)
	transformFilter.SetInputConnection(stl_reader_nac.GetOutputPort())
	transformFilter.Update()


	print('hi')

	stl_mapper_nac = vtk.vtkPolyDataMapper()
	stl_mapper_nac.SetInputConnection(transformFilter.GetOutputPort())

	stl_actor_nac = vtk.vtkActor()

	stl_actor_nac.GetProperty().SetOpacity(1)
	stl_actor_nac.SetMapper(stl_mapper_nac)

	# assembly.AddPart(stl_actor_nac)
	# assembly.RemovePart(stl_actor_nac)
	if m == 0:
		ren.AddActor(stl_actor_nac)

	m = m + 10
	print(m)
	

	renWin.Render()



assembly = vtk.vtkAssembly()
assembly2 = vtk.vtkAssembly()
assembly3 = vtk.vtkAssembly()


nonMovingfilenames = [ 
		"/Users/richardfindlay/Desktop/windTurbine/mesh/NewOrigin_Test/New_Origin_tower_Tower2.stl",
		"/Users/richardfindlay/Desktop/windTurbine/mesh/NewOrigin_Test/New_Origin_Nacelle2.stl",
		"/Users/richardfindlay/Desktop/windTurbine/mesh/NewOrigin_Test/New_Origin_Cylinder_002.stl"
	]


movingFilenames = [
	"/Users/richardfindlay/Desktop/windTurbine/mesh/NewOrigin_Test/New_Origin_Hub2.stl",
	"/Users/richardfindlay/Desktop/windTurbine/mesh/NewOrigin_Test/New_Origin_blade1-cap.stl",
	"/Users/richardfindlay/Desktop/windTurbine/mesh/NewOrigin_Test/New_Origin_blade1-pressureSide1.stl",
	"/Users/richardfindlay/Desktop/windTurbine/mesh/NewOrigin_Test/New_Origin_blade1-pressureSide2.stl",
	"/Users/richardfindlay/Desktop/windTurbine/mesh/NewOrigin_Test/New_Origin_blade1-suctionSide1.stl",
	"/Users/richardfindlay/Desktop/windTurbine/mesh/NewOrigin_Test/New_Origin_blade1-suctionSide2.stl",
	"/Users/richardfindlay/Desktop/windTurbine/mesh/NewOrigin_Test/New_Origin_blade2-cap.stl",
	"/Users/richardfindlay/Desktop/windTurbine/mesh/NewOrigin_Test/New_Origin_blade2-pressureSide1.stl",
	"/Users/richardfindlay/Desktop/windTurbine/mesh/NewOrigin_Test/New_Origin_blade2-pressureSide2.stl",
	"/Users/richardfindlay/Desktop/windTurbine/mesh/NewOrigin_Test/New_Origin_blade2-suctionSide1.stl",
	"/Users/richardfindlay/Desktop/windTurbine/mesh/NewOrigin_Test/New_Origin_blade2-suctionSide2.stl",
	"/Users/richardfindlay/Desktop/windTurbine/mesh/NewOrigin_Test/New_Origin_blade3-cap.stl",
	"/Users/richardfindlay/Desktop/windTurbine/mesh/NewOrigin_Test/New_Origin_blade3-pressureSide1.stl",
	"/Users/richardfindlay/Desktop/windTurbine/mesh/NewOrigin_Test/New_Origin_blade3-pressureSide2.stl",
	"/Users/richardfindlay/Desktop/windTurbine/mesh/NewOrigin_Test/New_Origin_blade3-suctionSide1.stl",
	"/Users/richardfindlay/Desktop/windTurbine/mesh/NewOrigin_Test/New_Origin_blade3-suctionSide2.stl"
]



for filename in nonMovingfilenames:
    stl_reader = vtk.vtkSTLReader()
    stl_reader.SetFileName(filename)

    stl_mapper = vtk.vtkPolyDataMapper()
    stl_mapper.SetInputConnection(stl_reader.GetOutputPort())

    stl_actor = vtk.vtkActor()
    # if filename == "/Users/richardfindlay/Desktop/windTurbine/mesh/non/nacelle.stl":
    #     stl_actor.GetProperty().SetColor(0.86,0.08,0.24)
    # else:
    stl_actor.GetProperty().SetOpacity(1)
    stl_actor.SetMapper(stl_mapper)

    assembly.AddPart(stl_actor)



for filename in movingFilenames:
    stl_reader2 = vtk.vtkSTLReader()
    stl_reader2.SetFileName(filename)

    stl_mapper2 = vtk.vtkPolyDataMapper()
    stl_mapper2.SetInputConnection(stl_reader2.GetOutputPort())

    stl_actor2 = vtk.vtkActor()
    # if filename == "/Users/richardfindlay/Desktop/windTurbine/mesh/non/nacelle.stl":
    #     stl_actor.GetProperty().SetColor(0.86,0.08,0.24)
    # else:
    stl_actor2.GetProperty().SetOpacity(1)
    stl_actor2.SetMapper(stl_mapper2)

    assembly2.AddPart(stl_actor2)

assembly.AddPart(assembly2)








# #add nacelle seperately
# stl_reader3 = vtk.vtkSTLReader()
# stl_reader3.SetFileName("/Users/richardfindlay/Desktop/windTurbine/mesh/non/nacelle.stl")

# stl_mapper3 = vtk.vtkPolyDataMapper()
# stl_mapper3.SetInputConnection(stl_reader3.GetOutputPort())

# stl_actor3 = vtk.vtkActor()
# # if filename == "/Users/richardfindlay/Desktop/windTurbine/mesh/non/nacelle.stl":
# #     stl_actor.GetProperty().SetColor(0.86,0.08,0.24)
# # else:
# stl_actor3.GetProperty().SetOpacity(1)
# stl_actor3.SetMapper(stl_mapper3)

# assembly.AddPart(stl_actor3)

camera = vtk.vtkCamera()
camera.SetPosition(0,0,10000)
camera.SetFocalPoint(0, 0, 0)

ren = vtk.vtkRenderer()
# ren.SetActiveCamera(camera)

renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
 
#Create a renderwindowinteractor
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

ren.AddActor(assembly)
# # ren.SetBackground(1,1,1)





# #find the centre of the hub
# actor_reader = vtk.vtkSTLReader()
# actor_reader.SetFileName("/Users/richardfindlay/Desktop/windTurbine/mesh//hub.stl")
# actortest_mapper = vtk.vtkPolyDataMapper()
# actortest_mapper.SetInputConnection(actor_reader.GetOutputPort())

# actor_test = vtk.vtkActor()
# actor_test.GetProperty().SetOpacity(1)
# actor_test.SetMapper(stl_mapper3)


# print(assembly.GetPosition())
# print(assembly.GetBounds())
# print(actor_test.GetCenter())

# bounds = assembly.GetBounds()

# center = np.zeros((3))
# center[0] = (bounds[1] + bounds[0]) / 2.0;
# center[1] = (bounds[3] + bounds[2]) / 2.0;
# center[2] = (bounds[5] + bounds[4]) / 2.0;

# print(center)

# stl_reader4 = vtk.vtkSTLReader()
# stl_reader4.SetFileName("/Users/richardfindlay/Desktop/windTurbine/mesh//hub.stl")

# import numpy
# # from stl import mesh
# import trimesh

# # mesh = mesh.Mesh.from_file('/Users/richardfindlay/Desktop/windTurbine/mesh//hub.stl')
# # volume, cog, inertia = mesh.get_mass_properties()
# mesh = trimesh.load("/Users/richardfindlay/Desktop/windTurbine/mesh/Test/rotationreference.stl")
# t = mesh.center_mass
# # print(t)


# c = actor_test.GetCenter() 

# transform = vtk.vtkTransform()
# # transform.Translate(-center[0], -center[1], -center[2])
# # transform.RotateWXYZ(180,1,0,0)
# transform.Translate(-t[0], -t[-1], -t[-2])
# transform.RotateWXYZ(180,1,0,0)
# transform.Translate(t[0], t[-1], t[-2])
# # transform.Translate(center[0], center[1], center[2])
# transformFilter=vtk.vtkTransformPolyDataFilter()
# transformFilter.SetTransform(transform)
# transformFilter.SetInputConnection(stl_reader4.GetOutputPort())
# transformFilter.Update()

# mapper1 = vtk.vtkPolyDataMapper()
# mapper1.SetInputConnection(transformFilter.GetOutputPort())

# stl_actor4 = vtk.vtkActor()
# stl_actor4.GetProperty().SetOpacity(1)
# stl_actor4.SetMapper(mapper1)


# # stl_actor3.SetCenter(c[0], c[1], c[2])
# assembly.AddPart(stl_actor4)

# def RotateAboutAxis(assembly2,timer_event):

# 	stl_reader_tower = vtk.vtkSTLReader()
# 	stl_reader_tower.SetFileName("/Users/richardfindlay/Desktop/windTurbine/mesh/NewOrigin_Test/New_Origin_tower_Tower2.stl")

# 	stl_mapper_tower = vtk.vtkPolyDataMapper()
# 	stl_mapper_tower.SetInputConnection(stl_reader_tower.GetOutputPort())

# 	stl_actor_tower = vtk.vtkActor()

# 	stl_actor_tower.GetProperty().SetOpacity(1)
# 	stl_actor_tower.SetMapper(stl_mapper_tower)

# 	centerYAW = stl_actor_tower.GetCenter()

# 	transform = assembly2.GetUserTransform()
# 	transform.Translate(centerYAW[0], centerYAW[1], centerYAW[2])
# 	transform.RotateWXYZ(1, 0, 1, 0)
# 	transform.Translate(-centerYAW[0], -centerYAW[1], -centerYAW[2])

# 	renWin.Render()


stl_reader_tower = vtk.vtkSTLReader()
stl_reader_tower.SetFileName("/Users/richardfindlay/Desktop/windTurbine/mesh/NewOrigin_Test/New_Origin_tower_Tower2.stl")

stl_mapper_tower = vtk.vtkPolyDataMapper()
stl_mapper_tower.SetInputConnection(stl_reader_tower.GetOutputPort())

stl_actor_tower = vtk.vtkActor()

stl_actor_tower.GetProperty().SetOpacity(1)
stl_actor_tower.SetMapper(stl_mapper_tower)



stl_reader_nac = vtk.vtkSTLReader()
stl_reader_nac.SetFileName("/Users/richardfindlay/Desktop/windTurbine/mesh/NewOrigin_Test/New_Origin_Nacelle2.stl")



centerYAW = stl_actor_tower.GetCenter()



iren.Initialize()
iren.CreateRepeatingTimer(5)
iren.AddObserver("TimerEvent", callback_function)
# iren.AddObserver("TimerEvent", callback_function2)
ren.SetBackground(0.14118,0.17647,0.21176)


# Enable user interface interactor
# iren.Initialize()
renWin.Render()
iren.Start()







